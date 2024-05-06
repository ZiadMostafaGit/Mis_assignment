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
    try:
        # Extract data from the request
        data = request.json
        c_p = data.get("c_p")
        p_id = data.get("p_id")
        orderData = data.get("orderData")

        # Validate the received data
        if not all(isinstance(item, int) for item in [c_p, p_id]) or not isinstance(orderData, list):
            return jsonify({"error": "Invalid request data"}), 400

        # Prepare the list of tuples for processing
        table = [(item.get("m_id"), item.get("quantitySold")) for item in orderData]

        # Call the sell_order function from the backend with the received data
        query = so.sell_order(c_p, p_id, table)

        return jsonify({"success_message": query}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == "__main__":
    app.run()


