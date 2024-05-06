import sqlite3
from datetime import datetime

def sell_order(c_id, p_id, medicines):
    try:
        conn = sqlite3.connect("pharma.db")
        cursor = conn.cursor()

        cursor.execute('''SELECT C_ID FROM Customer WHERE C_ID = ?''', (c_id,))
        customer_exists = cursor.fetchone()
        if not customer_exists:
            print(f"Customer with ID {c_id} does not exist.")
            return False

        cursor.execute('''SELECT P_ID FROM Pharmacist WHERE P_ID = ?''', (p_id,))
        pharmacist_exists = cursor.fetchone()
        if not pharmacist_exists:
            print(f"Pharmacist with ID {p_id} does not exist.")
            return False

        total = 0

        cursor.execute('''INSERT INTO "Order" (C_ID, P_ID, Total, Time)
                          VALUES (?, ?, ?, ?)''',
                       (c_id, p_id, total, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        order_id = cursor.lastrowid

        for medicine_id, quantity in medicines:
            cursor.execute('''SELECT M_Name, Unit_Price, Quantity FROM Medicine WHERE M_ID = ?''', (medicine_id,))
            result = cursor.fetchone()
            if result:
                medicine_name, unit_price, available_quantity = result
                if available_quantity >= quantity:
                    medicine_total = unit_price * quantity
                    total += medicine_total
                    cursor.execute('''INSERT INTO include (Medicine_ID, Order_ID, Quantity)
                                      VALUES (?, ?, ?)''',
                                   (medicine_id, order_id, quantity))
                    updated_quantity = available_quantity - quantity
                    cursor.execute('''UPDATE Medicine SET Quantity = ? WHERE M_ID = ?''', (updated_quantity, medicine_id))
                else:
                    print(f"Not enough quantity available for {medicine_name}.")
                    conn.rollback()
                    return False
            else:
                print(f"Medicine with ID {medicine_id} does not exist in the database.")
                conn.rollback()
                return False

        cursor.execute('''UPDATE "Order" SET Total = ? WHERE O_ID = ?''', (total, order_id))
        conn.commit()
        print("Order placed successfully!")
        return True

    except sqlite3.Error as e:
        print("Error placing order:", e)
        conn.rollback()
        return False

    finally:
        conn.close()

# c_id = 1
# p_id = 1
# medicines = [(69, 1),(121,5)] #(m_id ,qu)
# print(sell_order(c_id, p_id, medicines))
