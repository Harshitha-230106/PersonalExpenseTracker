from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def landingPage():
    return render_template("landingPage.html")

@app.route('/navbar')
def navbar():
    return render_template("Navbar.html")

@app.route('/contactus')
def contactus():
    return render_template("contactUs.html")

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # Handle signup logic
        pass
    return render_template("SignUp.html")

@app.route('/signin', methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        # Handle signin logic
        pass
    return render_template("SignIn.html")

@app.route('/aboutus')
def aboutus():
    return render_template("aboutUs.html")

if __name__ == '__main__':
    app.run(debug=True)

