from flask import Flask, render_template
import requests
import json

def call_API(foodName, apiKey):
    url = f'https://api.nal.usda.gov/fdc/v1/foods/search?api_key={apiKey}&query={foodName}'
    r = requests.get(url)
    print(r.status_code) 
    return r.json




