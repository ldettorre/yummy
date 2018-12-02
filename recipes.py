import os
from flask import Flask, render_template,redirect,request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")




mongo = PyMongo(app)

@app.route("/")
def get_index():
    return render_template("index.html")


@app.route("/get_recipe")
def get_recipe():
    recipes = mongo.db.recipes.find()
    return render_template("get_recipe.html", recipes=recipes)
    

@app.route("/add_recipe")
def add_recipe():
    cuisine = mongo.db.cuisine.find()
    return render_template("add_recipe.html", cuisine=cuisine) 
    
    
@app.route("/insert_recipe", methods=["POST"])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for("get_recipe")) 
    
    
@app.route("/edit_recipe/<recipe_id>")
def edit_recipe(recipe_id):
    _recipe = mongo.db.recipes.find_one({"_id":ObjectId(recipe_id)})
    _cuisine = mongo.db.cuisine.find()
    cuisine_list = [ cuisine for cuisine in _cuisine]
    return render_template("edit_recipe.html", recipe=_recipe, cuisine=cuisine_list)
        
@app.route("/update_recipe/<recipe_id>", methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update({"_id":ObjectId(recipe_id)},
    {
        "recipe_title" : request.form.get["recipe_title"],
        "recipe_cuisine" : request.form.get["recipe_cuisine"],
        "recipe_summary" : request.form.get["recipe_summary"],
        "recipe_ingredients" : request.form.get["recipe_ingredients"],
        "recipe_instructions" : request.form.get["recipe_instructions"],
        "recipe_portion" : request.form.get["recipe_portion"],
        "recipe_difficulty" : request.form.get["recipe_difficulty"],
        "recipe_preparation_time" : request.form.get["recipe_preparation_time"]
    })
    return redirect(url_for("get_recipe"))
    
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id":ObjectId(recipe_id)})
    return redirect(url_for("get_recipe"))
    
    
    # _recipe = mongo.db.recipes.find_one({"_id":ObjectId(recipe_id)})
    # _cuisine = mongo.db.cuisine.find()
    # cuisine_list = [ cuisine for cuisine in _cuisine]
    # return render_template("edit_recipe.html", recipe=_recipe, cuisine=cuisine_list)

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)),debug=True)
    