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
    return render_template("login-window.html")

@app.route("/about")
def about():
    return "This is a Music Quiz App!"

@app.route("/register")
def register():
    return render_template("register-window.html")




@app.errorhandler(404)
def http_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def http_internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(debug=True)


