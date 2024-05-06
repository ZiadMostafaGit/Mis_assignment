from flask import Flask, redirect, url_for, render_template, request,jsonify
import search as sh
import sell_order as so
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


@app.route("/Unavailable_Medications")
def Unavailable_Medications():
    return render_template("Unavailable_Medications.html")

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
    

@app.route('/search_purchases', methods=['POST'])
def perform_search_purches():
    search_query = request.form.get('search_purchases')
    results = sh.search_in_mid(search_query)
    return render_template('purchases.html', search_results=results)



    
@app.route('/search_sales', methods=['POST'])
def perform_search_sales():
    data = request.get_json()
    search_query = data.get('search_sales')
    if not search_query:
        # Handle the case when search_query is None or an empty string
        return jsonify([])

    results = sh.search_in_mid(search_query)
    return jsonify(results)
@app.route('/sell_order', methods=['POST'])
def sell_order():
    c_p = int(request.form.get("c_p"))
    p_id = int(request.form.get("p_id"))
    Id = int(request.form.get("id"))
    qu = int(request.form.get("Quantity"))
    table = [(Id, qu)]  # Creating a list containing a single tuple
    arr=[c_p,p_id,Id,qu,table]
    query = so.sell_order(c_p, p_id, table)
    test=str(arr)
    
    return render_template('sales.html', success_message=query,thedata=test)



if __name__ == "__main__":
    app.run()


