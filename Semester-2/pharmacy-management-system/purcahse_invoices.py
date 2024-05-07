import sqlite3

def fetch_purchase_invoices():
    conn = sqlite3.connect('pharma.db')
    cur = conn.cursor()

    try:
        cur.execute("""
            SELECT
                pm.Purchase_ID, pm.Medicine_ID, p.S_ID, m.M_Name,
                pm.Quantity AS total_quantity,
                m.Expire_Date,
                pm.purchase_price AS supplier_price,
                p.S_TotalPrice AS total
            FROM "Purchased_Medicine" pm
            JOIN "purchase" p ON pm.Purchase_ID = p.purchase_ID
            JOIN "Medicine" m ON pm.Medicine_ID = m.M_ID
            ORDER BY pm.Purchase_ID
        """)
        rows = cur.fetchall()

        invoices = []
        current_purchase_id = None
        current_invoice = None
        for row in rows:
            purchase_id, medicine_id, supplier_id, medicine_name, quantity, expire_date, supplier_price, total = row
            # Check if it's a new purchase ID
            if purchase_id != current_purchase_id:
                current_invoice = [purchase_id, supplier_id, total, []]
                invoices.append(current_invoice)
                current_purchase_id = purchase_id
            current_invoice[-1].append([medicine_id, medicine_name, quantity, expire_date, supplier_price])

        return invoices

    except sqlite3.Error as e:
        print("Error:", e)
        return []

    finally:
        conn.close()

# Example usage
purchase_invoices = fetch_purchase_invoices()
for invoice in purchase_invoices:
    print(invoice)




# Creation code of the tables :

# CREATE TABLE "Medicine" (
# 	"M_ID"	INTEGER,
# 	"M_Name"	TEXT NOT NULL UNIQUE,
# 	"Unit_Price"	REAL NOT NULL,
# 	"Quantity"	INTEGER NOT NULL,
# 	"Expire_Date"	TEXT NOT NULL,
# 	PRIMARY KEY("M_ID" AUTOINCREMENT),
# 	CHECK("Quantity" >= 0),
# 	CHECK("Unit_Price" >= 0)
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
# CREATE TABLE Supplier (
#   S_ID INTEGER PRIMARY KEY AUTOINCREMENT,
#   S_Name TEXT UNIQUE NOT NULL CHECK(LENGTH(S_Name) <= 50),
#   S_Phone TEXT UNIQUE NOT NULL CHECK(length(S_Phone) <= 11 AND S_Phone GLOB '[0-9]*')
# )
# CREATE TABLE "purchase" (
# 	"purchase_ID"	INTEGER,
# 	"S_ID"	INTEGER,
# 	"S_TotalPrice"	REAL,
# 	"S_Time"	TEXT,
# 	FOREIGN KEY("S_ID") REFERENCES "Supplier"("S_ID"),
# 	PRIMARY KEY("purchase_ID")
# )
# CREATE TABLE "Purchased_Medicine" (
# 	"Purchase_ID"	INTEGER,
# 	"Medicine_ID"	INTEGER,
# 	"Quantity"	INTEGER CHECK(quantity > 0),
# 	"purchase_price"	INTEGER,
# 	FOREIGN KEY("Purchase_ID") REFERENCES "purchase"("purchase_ID"),
# 	PRIMARY KEY("Purchase_ID","Medicine_ID"),
# 	FOREIGN KEY("Medicine_ID") REFERENCES "medicine"("M_ID")
# )