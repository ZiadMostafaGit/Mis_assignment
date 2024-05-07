import sqlite3  # Importing the sqlite3 module for working with SQLite databases

# Function to fetch sales invoices from a SQLite database
def fetch_sales_invoices():
    conn = sqlite3.connect('pharma.db')  # Establishing a connection to the 'pharma.db' SQLite database
    cur = conn.cursor()  # Creating a cursor object to execute SQL queries

    try:
        # Executing an SQL query to fetch sales invoice data by joining tables
        cur.execute("""
            SELECT
                o.O_ID, o.P_ID, o.C_ID, o.Total,  -- Selecting specific columns from the 'Order' table
                m.M_Name, i.Quantity, m.Unit_Price  -- Selecting specific columns from the 'Medicine' and 'include' tables
            FROM "Order" o  -- Selecting from the 'Order' table
            JOIN include i ON o.O_ID = i.Order_ID  -- Joining the 'include' table with 'Order' table on common key
            JOIN Medicine m ON i.Medicine_ID = m.M_ID  -- Joining the 'Medicine' table with 'include' table on common key
            ORDER BY o.O_ID  -- Ordering the results by Order ID
        """)
        rows = cur.fetchall()  # Fetching all the rows returned by the query into a list

        invoices = []  # Creating an empty list to store invoices
        # Iterating through each row fetched from the database
        for row in rows:
            # Unpacking the values from the current row
            order_id, pharmacist_id, customer_id, total, medicine_name, quantity, unit_price = row
            # Checking if the invoices list is empty or if the current row represents a new invoice
            if not invoices or order_id != invoices[-1][0]:
                # If it's a new invoice, appending a new sublist to the invoices list
                invoices.append([order_id, pharmacist_id, customer_id, total, []])
            # Appending the medicine details (name, quantity, unit price) to the current invoice
            invoices[-1][-1].append((medicine_name, quantity, unit_price))

        return invoices  # Returning the list of invoices

    except sqlite3.Error as e:  # Catching any SQLite errors that occur
        print("Error:", e)  # Printing the error message
        return []  # Returning an empty list in case of error

    finally:
        conn.close()  # Closing the database connection after the operation is complete


# Example usage
invoices = fetch_sales_invoices()  # Calling the fetch_sales_invoices function to get invoices
for invoice in invoices:  # Iterating through each invoice in the list of invoices
    print(invoice)  # Printing each invoice



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