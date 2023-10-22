import os
import requests
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, request

load_dotenv()

app = Flask(__name__)
API_KEY = os.environ.get("API_KEY")


@app.route("/")
def home():
    return render_template("index.html", city="", data="")


@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        city = request.form.get("city")
        units = request.form.get("units")

        response = requests.get(
            url="https://api.openweathermap.org/data/2.5/weather",
            params={"q": city, "units": units, "appid": API_KEY},
        )

        if response.status_code == 200:
            data = response.json()
            return render_template("index.html", city=data["name"], data=data)

        return render_template("index.html", city="", data="Bad Request")

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
