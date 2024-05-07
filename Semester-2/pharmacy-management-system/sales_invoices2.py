import sqlite3  # Import the sqlite3 module for working with SQLite databases

# Define a function to fetch sales invoices from a SQLite database
def fetch_sales_invoices():
    conn = sqlite3.connect('pharma.db')  # Establish a connection to the 'pharma.db' SQLite database
    cur = conn.cursor()  # Create a cursor object to execute SQL queries

    try:
        cur.execute("""  -- Execute a SQL query to select data from multiple tables
            SELECT
                o.O_ID, o.P_ID, o.C_ID,
                m.M_Name, i.Quantity, m.Unit_Price,
                o.Total,
                p.P_Name AS Pharmacist_Name,
                c.C_Name AS Customer_Name
            FROM "Order" o
            JOIN include i ON o.O_ID = i.Order_ID
            JOIN Medicine m ON i.Medicine_ID = m.M_ID
            JOIN Pharmacist p ON o.P_ID = p.P_ID
            JOIN Customer c ON o.C_ID = c.C_ID
            ORDER BY o.O_ID
        """)
        rows = cur.fetchall()  # Fetch all the rows returned by the query
        invoices = []  # Create an empty list to store invoice data

        # Iterate over each row fetched from the query result
        for row in rows:
            # Unpack values from the row into variables
            order_id, pharmacist_id, customer_id, medicine_name, quantity, unit_price, total, pharmacist_name, customer_name = row

            # Check if invoices list is empty or if the current order_id is different from the last invoice's order_id
            if not invoices or order_id != invoices[-1]["order_id"]:
                # If it's a new invoice, append a new dictionary representing the invoice to the invoices list
                invoices.append({
                    "order_id": order_id,
                    "customer_name": customer_name,
                    "pharmacist_name": pharmacist_name,
                    "total": "{:.2f}".format(total),  # Format total with 2 decimal places
                    "medicines": []  # Create an empty list to store medicine details for this invoice
                })
            # Append medicine details to the last invoice in the invoices list
            invoices[-1]["medicines"].append({
                "medicine_name": medicine_name,
                "quantity": quantity,
                "unit_price": "{:.2f}".format(unit_price)  # Format unit price with 2 decimal places
            })
        return invoices  # Return the list of invoices

    except sqlite3.Error as e:  # Catch any SQLite database errors
        print("Error:", e)  # Print the error message
        return []  # Return an empty list indicating failure

    finally:
        conn.close()  # Close the database connection when finished

# Example usage
invoices = fetch_sales_invoices()  # Call the fetch_sales_invoices function to retrieve invoices
for invoice in invoices:  # Iterate over each invoice in the list of invoices
    print(invoice)  # Print the details of each invoice



# Creation code of the tables :

# CREATE TABLE Customer (
#   C_ID INTEGER PRIMARY KEY AUTOINCREMENT,
#   C_Name TEXT UNIQUE NOT NULL CHECK(LENGTH(C_Name) <= 50),
#   C_Phone TEXT UNIQUE NOT NULL CHECK(length(C_Phone) <= 11 AND C_Phone GLOB '[0-9]*')
# )
# CREATE TABLE "Medicine" (
# 	"M_ID"	INTEGER,
# 	"M_Name"	TEXT NOT NULL UNIQUE,
# 	"Unit_Price"	REAL NOT NULL,
# 	"Quantity"	INTEGER NOT NULL,
# 	"Expire_Date"	TEXT NOT NULL,
# 	PRIMARY KEY("M_ID" AUTOINCREMENT),
# 	CHECK("Quantity" >= 0),
# 	CHECK("Unit_Price" >= 0)
# )
# CREATE TABLE "Order" (
# 	"O_ID"	INTEGER,
# 	"C_ID"	INTEGER,
# 	"P_ID"	INTEGER,
# 	"Total"	REAL,
# 	"Time"	DATETIME DEFAULT (DATETIME('now', 'localtime')),
# 	PRIMARY KEY("O_ID" AUTOINCREMENT),
# 	FOREIGN KEY("P_ID") REFERENCES "Pharmacist"("P_ID"),
# 	FOREIGN KEY("C_ID") REFERENCES "Customer"("C_ID")
# )
# CREATE TABLE Pharmacist (
#   P_ID INTEGER PRIMARY KEY AUTOINCREMENT,
#   P_Name TEXT UNIQUE NOT NULL CHECK(LENGTH(P_Name) <= 50)
# )
# CREATE TABLE include (
#   Medicine_ID INTEGER,
#   Order_ID INTEGER,
#   Quantity INTEGER,
#   PRIMARY KEY (Medicine_ID, Order_ID),
#   FOREIGN KEY (Medicine_ID) REFERENCES medicine(M_ID),
#   FOREIGN KEY (Order_ID) REFERENCES "order"(O_ID)
# )
