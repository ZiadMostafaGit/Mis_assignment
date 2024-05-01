from flask import Flask, redirect, url_for, render_template, request,jsonify
import search as sh
app = Flask(__name__)

@app.route("/")
def home():
    error_message = request.args.get("error_message")
    return render_template("Home.html", error_message=error_message)

@app.route("/purchases_invoices")
def purchases_invoices():
    return render_template("purchases_invoices.html")

@app.route("/purchases")
def purchases():
    return render_template("purchases.html")

@app.route("/sales_invoices")
def sales_invoices():
    return render_template("Sales_invoices.html")

@app.route("/sales")
def sales():
    return render_template("sales.html")





@app.route("/cash")
def cash():
    return render_template("cash.html")


@app.route("/expiring")
def expiring():
    return render_template("expiring.html")

@app.route("/inventory")
def inventory():
    return render_template("inventory.html")

@app.route("/missing")
def missing():
    return render_template("missing.html")



@app.route("/login", methods=["POST"])
def login():
    password = request.form.get("password")
    if password == "admin123":
        return redirect(url_for("sales"))  # Redirect to sales page if login is successful
    else:
        error_message = "Incorrect password. Please try again."
        return redirect(url_for("home", error_message=error_message))
    

@app.route('/search', methods=['POST'])
def perform_search():
    search_query = request.form.get('search')
    results = sh.search_in_mid(search_query)
    return render_template('purchases.html', search_results=results)

if __name__ == "__main__":
    app.run()
