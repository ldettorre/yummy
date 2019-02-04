import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_bcrypt import bcrypt



app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.secret_key = os.urandom(24)


mongo = PyMongo(app)

@app.route("/")
def get_index():
    if "username" in session:
        return render_template("index.html")
        
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    users = mongo.db.users.find()
    user_login = request.form.get("username")
    # Credit to Michael Park for helping me solve my login issue below using a list
    names = [] 
    for u in users:
        if u["username"]:
            names.append(u["username"])
    
    if user_login in names:
        session["username"] = user_login
        return redirect(url_for("get_userpage", username=user_login))
    else:
        flash("This is an incorrect username.")
        return redirect(url_for("get_index"))
   

    
    
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("get_index"))

    
@app.route("/register", methods=["POST","GET"])
def register():
    if request.method == "POST":
        users = mongo.db.users
        existing_users = users.find_one({"username":request.form.get("username")})
        
        if existing_users is None:
            users.insert({"username": request.form.get("username")})
            session["username"] = request.form.get("username")
            return redirect (url_for("get_index"))
        
        flash("This Username is unavailable.")
        return redirect(url_for("get_index"))
    return render_template("index.html")
        
        
@app.route("/<username>") 
def get_userpage(username):
    username = session["username"]
    recipes = mongo.db.recipes.find()
    return render_template("userpage.html", username=username, recipes=recipes)

@app.route("/mexican_recipes")
def mexican_recipes():
    recipes = mongo.db.recipes.find({"recipe_cuisine":"mexican"})
    return render_template("get_recipe.html", recipes = recipes) 
    
@app.route("/brazilian_recipes")
def brazilian_recipes():
    recipes = mongo.db.recipes.find({"recipe_cuisine":"brazilian"})
    return render_template("get_recipe.html", recipes = recipes) 
    
@app.route("/italian_recipes")
def italian_recipes():
    recipes = mongo.db.recipes.find({"recipe_cuisine":"italian"})
    return render_template("get_recipe.html", recipes = recipes) 
    
@app.route("/chinese_recipes")
def chinese_recipes():
    recipes = mongo.db.recipes.find({"recipe_cuisine":"chinese"})
    return render_template("get_recipe.html", recipes = recipes) 
    


#----- Recipe Functions -----#

@app.route("/show-recipe/<recipe_id>")
def show_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("show-recipe.html" , recipe=recipe)

@app.route("/get_recipe")
def get_recipe():
    recipes = mongo.db.recipes.find()
    recipes_total = mongo.db.recipes.find().sort("recipe_title").count()
    return render_template("get_recipe.html", recipes=recipes,recipes_total=recipes_total)
    

@app.route("/add_recipe")
def add_recipe():
    cuisine = mongo.db.cuisine.find()
    if "username" in session:
        return render_template("add_recipe.html", cuisine=cuisine) 
    else: 
        flash("Please log in to use this feature.")
        return render_template("index.html")
   
    
@app.route("/insert_recipe", methods=["POST"])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    # The two lines below copy the recipe author value out of the recipe form and saves it to a seperate
    # collection called Authors for further uses
    authors = mongo.db.authors
    authors.insert_one({"recipe_author" : request.form.get("recipe_author")})
    return redirect(url_for("get_recipe", recipes=recipes)) 
    
    
@app.route("/edit_recipe/<recipe_id>")
def edit_recipe(recipe_id):
    _recipe = mongo.db.recipes.find_one({"_id":ObjectId(recipe_id)})
    _cuisine = mongo.db.cuisine.find()
    cuisine_list = [ cuisine for cuisine in _cuisine]
    return render_template("edit_recipe.html", recipe=_recipe, cuisine=cuisine_list)


@app.route("/update_recipe/<recipe_id>", methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update(
        {"_id":ObjectId(recipe_id)},
    {
        "recipe_title" : request.form.get("recipe_title"),
        "recipe_editor" : request.form.get("recipe_editor"),
        "recipe_author" : request.form.get("recipe_author"),
        "recipe_status" : request.form.get("recipe_status"),
        "recipe_cuisine" : request.form.get("recipe_cuisine"),
        "recipe_summary" : request.form.get("recipe_summary"),
        "recipe_ingredients" : request.form.get("recipe_ingredients"),
        "recipe_instructions" : request.form.get("recipe_instructions"),
        "recipe_portion" : request.form.get("recipe_portion"),
        "recipe_difficulty" : request.form.get("recipe_difficulty"),
        "recipe_preparation_time" : request.form.get("recipe_preparation_time"),
        "recipe_cooking_time" : request.form.get("recipe_cooking_time")
        
    })
    authors = mongo.db.authors
    authors.insert_one({"recipe_author" : request.form.get("recipe_author")})
    return redirect(url_for("get_recipe"))
    
    
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id":ObjectId(recipe_id)})
    return redirect(url_for("get_recipe"))
    
    
#----- Cuisine Functions -----#

@app.route("/list_cuisines")
def list_cuisines():
    cuisines = mongo.db.cuisine.find().sort("recipe_cuisine")
    return render_template("list_cuisines.html", cuisines=cuisines)
    
    
@app.route("/get_cuisines/<cuisine_id>")
def get_cuisines(cuisine_id):
    selected_cuisine = mongo.db.cuisine.find_one({"_id": ObjectId(cuisine_id)})
    selected_cuisine_recipes = mongo.db.recipes.find({"recipe_cuisine":selected_cuisine["recipe_cuisine"]})
    
    return render_template("filter_cuisines.html", selected_cuisine_recipes=selected_cuisine_recipes ) 

    
@app.route("/add_cuisine")
def add_cuisine():
    cuisine = mongo.db.cuisine.find()
    return render_template("add_cuisine.html", cuisine=cuisine) 

    

@app.route("/insert_cuisine", methods=["POST","GET"])
def insert_cuisine():
    if request.method == "POST":
        cuisines = mongo.db.cuisine
        existing_cuisines = cuisines.find_one({"recipe_cuisine":request.form.get("recipe_cuisine").lower()})
        
        if existing_cuisines is None:
            cuisines.insert(({"recipe_cuisine": request.form.get("recipe_cuisine").lower()}))
            return redirect(url_for("list_cuisines", cuisines=cuisines))
        
        flash("This cuisine already exists.")
        return redirect(url_for("list_cuisines"))
    return render_template("list_cuisines.html")


@app.route("/delete_cuisine/<cuisine_id>")
def delete_cuisine(cuisine_id):
    mongo.db.cuisine.remove({"_id":ObjectId(cuisine_id)})
    return redirect(url_for("get_cuisines"))
    
    
@app.route("/update_cuisine/<cuisine_id>", methods=["POST"])
def update_cuisine(cuisine_id):
    cuisine = mongo.db.cuisine
    cuisine.update(
        {"_id":ObjectId(cuisine_id)},
        {"recipe_cuisine" : request.form.get("recipe_cuisine")})
    return redirect(url_for("get_cuisines"))



#----- Author Functions -----#

@app.route("/all_authors")
def all_authors():
    authors = mongo.db.authors.find().sort("recipe_author")
    author_total = mongo.db.authors.find().sort("recipe_author").count()
    return render_template("all_authors.html", authors=authors, author_total=author_total)


@app.route("/authors_recipes/<author_id>")  
def authors_recipes(author_id):
    selected_author = mongo.db.authors.find_one({"_id":ObjectId(author_id)})
    selected_authors_recipes = mongo.db.recipes.find({"recipe_author":selected_author["recipe_author"]})
        
    return render_template("recipe_by_author.html", selected_authors_recipes=selected_authors_recipes )

if __name__ == "__main__":
    app.run(host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 8080)),debug=True)
    