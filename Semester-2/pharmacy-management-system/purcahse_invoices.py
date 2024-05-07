import sqlite3
def fetch_purchase_invoices():
    conn = sqlite3.connect('pharma.db')
    cur = conn.cursor()

    try:
        cur.execute("""
            SELECT
                p.Purchase_ID, p.S_ID, p.S_TotalPrice,
                pm.Medicine_ID, m.M_Name, pm.Quantity,
                m.Expire_Date
            FROM "purchase" p
            JOIN "Purchased_Medicine" pm ON p.purchase_ID = pm.Purchase_ID
            JOIN "Medicine" m ON pm.Medicine_ID = m.M_ID
            ORDER BY p.Purchase_ID
        """)
        rows = cur.fetchall()

        invoices = []
        current_purchase_id = None
        current_invoice = None
        for row in rows:
            purchase_id, supplier_id, total_price, medicine_id, medicine_name, quantity, expire_date = row
            if purchase_id != current_purchase_id:
                if current_invoice:
                    invoices.append(current_invoice)
                current_invoice = [purchase_id, supplier_id, total_price, []]
                current_purchase_id = purchase_id
            current_invoice[3].append([medicine_id, medicine_name, quantity, total_price, expire_date])

        if current_invoice:
            invoices.append(current_invoice)

        return invoices

    except sqlite3.Error as e:
        print("Error:", e)
        return []

    finally:
        conn.close()


print(fetch_purchase_invoices())