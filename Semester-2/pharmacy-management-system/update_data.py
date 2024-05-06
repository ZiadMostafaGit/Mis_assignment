import sqlite3
def update_data(table, condition_column, condition_value, column, new_value):
    try:
        conn = sqlite3.connect('pharma.db')
        cursor = conn.cursor()

        query = f"UPDATE {table} SET {column} = ? WHERE {condition_column} = ?"
        cursor.execute(query, (new_value, condition_value))

        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print(f"Error updating data: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Test the update_data function to modify a specific record
table='customer'
column='C_Phone'
new_value='00100000'
condition_column='C_id'
condition_value=2

update_data(table, condition_column, condition_value, column, new_value)