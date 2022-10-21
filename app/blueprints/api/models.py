from flask import Flask, render_template, request
import requests


app = Flask(__name__)

food_data = {
    0: {
        "name": "apple",
        "macros": {
          "oz": 1,
          "calories": 15,
          "protein": 0.1,
          "carbs": 1.9,
          "fat": 0
          }
    },
    1: {
        "name": "orange",
        "macros": {
          "oz": 1,
          "calories": 13,
          "protein": 0.3,
          "carbs": 3.3,
          "fat": 0
        }
    },
    2: {
        "name": "banana",
        "macros": {
          "oz": 1,
          "calories": 25,
          "protein": 0.3,
          "carbs": 6.5,
          "fat": 0.1
        }
    },
    3: {
        "name": "brussel sprouts",
        "macros": {
          "oz": 1,
          "calories": 12,
          "protein": 1,
          "carbs": 2.5,
          "fat": 0.1
        }
    },
    4: {
        "name": "zucchini",
        "macros": { 
          "oz": 1,
          "calories": 5,
          "protein": 0.1,
          "carbs": 0.9,
          "fat": 0.1
        }
    },
    5: {
        "name": "bell papper",
        "macros": {
          "oz": 1,
          "calories": 6,
          "protein": 0.2,
          "carbs": 1.3,
          "fat": 0
          }
    },
    6: {
        "name": "almonds",
        "macros": {
          "oz": 1,
          "calories": 164,
          "protein": 6,
          "carbs": 6.1,
          "fat": 14.2
        }
    },
    7: {
        "name": "chicken",
        "macros": {
          "oz": 3.5,
          "calories": 284,
          "protein": 53.4,
          "carbs": 0,
          "fat": 6.2
          }
    },
    8: {
        "name": "green beans",
        "macros": {
          "oz": 8,
          "calories": 100,
          "protein": 1.8,
          "carbs": 7,
          "fat": 0.2
        }
    },
    9: {
        "name": "carrot",
        "macros": {
          "oz": 3,
          "calories": 28,
          "protein": 0.5,
          "carbs": 6,
          "fat": 1
        }
    },
    10: {
        "name": "beef tenderlion",
        "macros": {
          "oz": 3,
          "calories": 168,
          "protein": 26.1,
          "carbs": 0,
          "fat": 7.1
        }
    }
}

@app.route('/foods')
def foods():
    return food_data




















""" 
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
  if (str(request.args['ingredients']).strip() != ""):
      querystring = {"number":"5","ranking":"1","ignorePantry":"false","ingredients":request.args['ingridients']}
      response = requests.request("GET", url + find, headers=headers, params=querystring).json()
      return render_template('recipes.html', recipes=response)
  else:
      querystring = {"number":"5"}
      response = requests.request("GET", url + randomFind, headers=headers, params=querystring).json()
      print(response)
      return render_template('recipes.html', recipes=response['recipes']) """