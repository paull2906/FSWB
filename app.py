from pathlib import Path

from flask import Flask, render_template

BASE_DIR = Path(__file__).resolve().parent

app = Flask(
    __name__,
    template_folder=BASE_DIR / "templates",
    static_folder=BASE_DIR / "static",
)

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/about")
def about():
    return "This is a Music Quiz App!"

if __name__ == "__main__":
    app.run(debug=True)
