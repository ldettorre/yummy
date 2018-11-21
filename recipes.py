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
def get_recipes():
    recipes = mongo.db.recipes.find()
    recipe_list = [recipe for recipe in recipes]
    return render_template("recipes.html", recipes=recipe_list)


@app.route("/add_recipe")
def add_recipes():
    # recipes = mongo.db.recipes.find()
    # recipe_list = [recipe for recipe in recipes]
    return render_template("addrecipe.html")   


if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)),debug=True)