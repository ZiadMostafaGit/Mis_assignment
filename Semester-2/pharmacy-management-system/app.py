from flask import Flask,redirect,url_for


app=Flask(__name__)

@app.route("/")
def Home():
    return "Hello world my first flask app is running"

@app.route("/<name>")
def user(name):
    return f"hello {name}"


@app.route("/admin")
def admin():
    return redirect(url_for("Home"))

@app.route("/uthuntcate")
def uthuntcate():
    return f"this page is for admin and its private"



if __name__=="__main__":
    app.run()

