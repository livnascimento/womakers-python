from flask import Flask, render_template, url_for
import urllib.request, json

app = Flask(__name__)

@app.route("/")
def get_characters():
    url = "https://hp-api.onrender.com/api/characters"

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("characters.html", characters = dict)
