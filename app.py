from flask import Flask, render_template, request, redirect, url_for, session

import matplotlib.pyplot as plt
import numpy as np
import io
import base64



# Initialize Flask app
app = Flask(__name__)
app.secret_key = "mysecretkey"  # Used to store session data securely


# Define routes for different pages
@app.route('/')
@app.route("/")
def home():
    if "progress" not in session:
        session["progress"] = 0  # Start at 0 (no sections unlocked)

    return render_template("index.html", progress=session["progress"])


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/games')
def games():
    return render_template('games.html')

@app.route("/game1", methods=["GET", "POST"])
def game1():
    if request.method == "POST":
        answer = request.form.get("answer", "").lower()
        if answer == "love":
            session["progress"] = 1  # Unlocks Gallery
            return redirect(url_for("home"))

    return render_template("game1.html")
@app.route("/game2", methods=["GET", "POST"])
def game2():
    if request.method == "POST":
        answer = request.form.get("answer", "").lower()
        if answer == "amore":  # Italian for "love"
            session["progress"] = 2  # Unlocks Memes section
            return redirect(url_for("home"))

    return render_template("game2.html")

@app.route("/graph")
def graph():

    # Generate heart-shaped graph
    t = np.linspace(0, 2 * np.pi, 100)
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

    plt.figure(figsize=(6, 6))
    plt.plot(x, y, 'r')
    plt.axis("off")

    # Save plot to an image
    img = io.BytesIO()
    plt.savefig(img, format="png", bbox_inches="tight")
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()

    print(graph_url[:50])  # Print the first 50 chars of the base64 string


    return render_template("graph.html", graph_url=graph_url)

@app.route("/valentine")
def valentine():
    poem = """
    My Northern Star<br><br>
    I feel safe around you—why is that so?<br>
    You’ve brought peace to this turbulent world of mine,<br>
    A marvel that I can't let go.<br><br>

    I feel comfortable with you—what is this, I ask?<br>
    You lull me to sleep in a flicker, like a baby,<br>
    When fear once kept me awake in the past.<br><br>

    I feel like I miss you every second—why, you may ask?<br>
    Your presence is the northern star in my night sky,<br>
    A wonder that makes the Darkness fly.<br><br>

    I feel thankful that we met—what do I mean?<br>
    I’m grateful you gave me my world—oh, it’s you, I mean.<br><br>

    I love you—this is plain, yet true.<br>
    In every breath I breathe,<br>
    And every beat my heart keeps,<br>
    It only ever spells you.<br><br>

    🌹 Will you be my Valentine, Rosie? ❤️
    """
    return render_template("valentine.html", poem=poem)

@app.route('/memes')
def memes():
    return render_template('memes.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)