import requests
import json
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import datetime
from flask import Flask, render_template, url_for, redirect, request

API = "1a5bdbc0ee6144dcb72131751242102"
aqi = "yes"


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    __tablename__ = "user"
id = db.Column(db.Integer, primary_key=True)
username = db.Column(db.String(50))
email = db.Column(db.String(120), unique=True, nullable=False)
password = db.Column(db.String(100), nullable=False)

@app.route("/")
def home():
    return render_template(login.html)

city_name = input("Enter city name to get its weather report: ")
url = f"http://api.weatherapi.com/v1/current.json?key={API}&q={city_name}&aqi={aqi}"
result = requests.get(url)
print(result)
wdata = json.loads(result.text)
print(wdata)

name = wdata["location"]["name"]
region = wdata["location"]["region"]
temp = wdata["current"]["temp_c"]
humidity = wdata["current"]["humidity"]
country = wdata["location"]["country"]
pressure = wdata["current"]["pressure_mb"]

print(pressure)
print(name)
print(humidity)
print(temp)
print(region)
print(country)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)