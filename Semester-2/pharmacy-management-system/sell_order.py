import sqlite3

def sell_order(c_id, p_id, medicines):
    from datetime import datetime
    ch = True
    try:
        conn = sqlite3.connect("pharma.db")
        cursor = conn.cursor()

        cursor.execute('''SELECT C_ID FROM Customer WHERE C_ID = ?''', (c_id,))
        customer_exists = cursor.fetchone()
        if not customer_exists:
            ch = False
            print(f"Customer with ID {c_id} does not exist.")
            return

        cursor.execute('''SELECT P_ID FROM Pharmacist WHERE P_ID = ?''', (p_id,))
        pharmacist_exists = cursor.fetchone()
        if not pharmacist_exists:
            ch = False
            print(f"Pharmacist with ID {p_id} does not exist.")
            return

        total = 0

        cursor.execute('''INSERT INTO "Order" (C_ID, P_ID, Total, Time)
                          VALUES (?, ?, ?, ?)''',
                       (c_id, p_id, total, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        order_id = cursor.lastrowid

        for medicine in medicines:
            medicine_id, quantity = medicine
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
                    ch = False
                    # print(f"Not enough quantity available for {medicine_name}.")
                    conn.close()
                    return False
            else:
                ch = False
                # print(f"Medicine with ID {medicine_id} does not exist in the database.")
                conn.close()
                return False
        if ch==True:
            cursor.execute('''UPDATE "Order" SET Total = ? WHERE O_ID = ?''', (total, order_id))

            conn.commit()
            # print("Order placed successfully!")
            conn.close()
            return True

    except sqlite3.Error as e:
        # print("Error placing order:", e)
        conn.close()
        return False

    finally:
        conn.close()

c_id = 1
p_id = 1
medicines = [(69, 200)] #(m_id ,qu)
print(sell_order(c_id, p_id, medicines))












# data = [(1, 'Eman abo-rehab', '02647356482'),
#         (2, 'Saad abd el samei', '00100000'),
#         (3, 'Rahma mohammed', '09867354267'),
#         (4, 'Eslam Amer', '06748365234'),
#         (5, 'Anwar EL-Sadat', '04736486534'),
#         (6, 'MOMO', '1234567890'),
#         (7, 'Customer ABC', '23423423')]

# # Targeting index 2
# target_index = 2
# if 0 <= target_index < len(data):
#     targeted_tuple = data[target_index]
#     name = targeted_tuple[2]  # Accessing the name at index 1
#     print(name)
# else:
#     print("Index is out of range.")
