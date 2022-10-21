from contextlib import redirect_stderr
from app import app
from flask import render_template, request, redirect, url_for, flash
from app import db
from flask_login import current_user


@app.route('/')
def home ():
    return render_template('home.html')

""" @app.route('/about')
def about():
    return render_template('about.html') """

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/online')
def online():
    return render_template('online.html')

@app.route('/inperson')
def inperson():
    return render_template('inperson.html')

@app.route('/food')
def food():
    return render_template('food.html')

@app.route('/food', methods=['POST'])
def food_data():
    food_data = request.form['name']
    macro_body = request.form['macros']
    print(food_data, macro_body)

    new_post = Food(name=food_data, body=macro_body, user_id=current_user.id)

    db.session.add(new_post)
    db.session.commit()

    flash('New food added', 'success')
    return redirect(url_for('home'))















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
  find = str(requests.requests("GET", url, headers=headers).json()['text'])
  return render_template('food.html')
if __name__ == '__main__':
  app.run()

@app.route('/recipes')
def get_recipes():
  if (str(request.args['ingredients']).strip() != ""):
      querystring = {"number":"5","ranking":"1","ignorePantry":"false","ingredients":request.args['ingredients']}
      response = requests.requests("GET", url + find, headers=headers, params=querystring).json()
      return render_template('recipes.html', recipes=response)
  else:
      querystring = {"number":"5"}
      response = requests.requests("GET", url + randomFind, headers=headers, params=querystring).json()
      print(response)
      return render_template('recipes.html', recipes=response['recipes'])
 """