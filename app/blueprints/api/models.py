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

@app.route('/recipes')
def get_recipes():
  if (str(request.args['ingridients']).strip() != ""):
      querystring = {"number":"5","ranking":"1","ignorePantry":"false","ingredients":request.args['ingridients']}
      response = requests.request("GET", url + find, headers=headers, params=querystring).json()
      return render_template('recipes.html', recipes=response)
  else:
      querystring = {"number":"5"}
      response = requests.request("GET", url + randomFind, headers=headers, params=querystring).json()
      print(response)
      return render_template('recipes.html', recipes=response['recipes'])