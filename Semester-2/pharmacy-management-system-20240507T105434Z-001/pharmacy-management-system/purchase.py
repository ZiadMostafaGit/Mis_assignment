import sqlite3
from datetime import datetime

def purchase_order(s_id, medicines):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect("pharma.db")
        cursor = conn.cursor()

        # Initialize total price for the purchase
        total_price = 0

        # Insert purchase into "purchase" table
        purchase_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute('''INSERT INTO "purchase" (S_ID, S_TotalPrice, S_Time)
                          VALUES (?, ?, ?)''',
                       (s_id, total_price, purchase_time))

        # Get the purchase ID of the newly inserted purchase
        purchase_id = cursor.lastrowid

        # Iterate through the list of medicines to purchase
        for medicine in medicines:
            medicine_id, quantity, purchase_price, expire_date = medicine
            # Check if medicine ID exists in the database
            cursor.execute('''SELECT M_Name, Quantity, Expire_Date FROM Medicine WHERE M_ID = ?''', (medicine_id,))
            result = cursor.fetchone()
            if result:
                medicine_name, available_quantity, current_expire_date = result
                # Add the purchased quantity to the available quantity
                updated_quantity = available_quantity + quantity
                # Update the quantity of the medicine in the Medicine table
                cursor.execute('''UPDATE Medicine SET Quantity = ?, Expire_Date = ? WHERE M_ID = ?''',
                               (updated_quantity, expire_date, medicine_id))
                # Insert the purchased medicine into "Purchased_Medicine" table
                cursor.execute('''INSERT INTO Purchased_Medicine (Purchase_ID, Medicine_ID, Quantity, Purchase_Price)
                                  VALUES (?, ?, ?, ?)''',
                               (purchase_id, medicine_id, quantity, purchase_price))
                # Calculate the total price for the purchase
                total_price += quantity * purchase_price
            else:
                print(f"Medicine with ID {medicine_id} does not exist in the database.")

        # Update total price in "purchase" table
        cursor.execute('''UPDATE "purchase" SET S_TotalPrice = ? WHERE Purchase_ID = ?''', (total_price, purchase_id))

        # Commit the transaction
        conn.commit()
        print("Purchase order completed successfully!")

    except sqlite3.Error as e:
        print("Error placing purchase order:", e)

    finally:
        # Close the connection
        conn.close()

# # Example usage
# s_id = 1  # Example supplier ID

# # Example medicines to purchase: (Medicine_ID, Quantity, Purchase_price, Expire_Date)
# medicines = [(226, 10, 5.5, '06/3/2026')]  # Example medicines to purchase with expire date

# # Call the function to place the purchase order
# purchase_order(s_id, medicines)



