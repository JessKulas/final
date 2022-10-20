from flask import Flask, render_template, request
import requests


app = Flask(__name__)

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/"

headers = {
  'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
  'API_KEY': "<API_KEY>",
  }

find = "recipes/findByIngredients"
randomFind = "recipes/random"
@app.route('/food')
def search_page():
  find = str(requests.request("GET", url, headers=headers).json()['text'])
  return render_template('food.html')
if __name__ == '__main__':
  app.run()
