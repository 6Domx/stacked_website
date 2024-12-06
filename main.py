from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
@app.route("/home")
def home():
    return render_template("home.html")

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route("/works")
def works():
    return render_template("works.html")

if __name__ == "__main__":
    app.run(debug=True)


