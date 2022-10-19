from flask import Flask, render_template


@app.route('/food')
def about():
    return 'https://api.spoonacular.com/recipes/findByIngredients?apiKey=0cccc974b5f047ecaad5564a64e53231'