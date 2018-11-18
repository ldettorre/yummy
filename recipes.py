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
    return "Welcome to the Homepage"


@app.route("/get_recipes")
def get_recipes():
    recipes = mongo.db.recipes.find()
    recipe_list = [recipe for recipe in recipes]
    return render_template("recipes.html", recipes=recipe_list)
    


if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))