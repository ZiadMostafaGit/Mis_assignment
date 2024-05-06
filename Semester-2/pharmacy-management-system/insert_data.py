import sqlite3

def insert_data(table_name, data):
    try:
        # Connect to the database (or create it if it doesn't exist)
        conn = sqlite3.connect('pharma.db')
        cur = conn.cursor()

        # Construct the insert query dynamically
        insert_query = f"INSERT INTO {table_name} ({','.join(data.keys())}) VALUES ({','.join(['?' for _ in data])})"

        # Check if the data already exists
        select_query = f"SELECT * FROM {table_name} WHERE {' AND '.join([f'{col}=?' for col in data.keys()])}"
        cur.execute(select_query, tuple(data.values()))
        existing_data = cur.fetchone()

        if existing_data:
            print("Data already exists.")
        else:
            cur.execute(insert_query, tuple(data.values()))

            # Commit the changes to the database
            conn.commit()

            print("Data inserted successfully!")

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the connection
        if conn:
            conn.close()
# Example usage
table_name = "purchase"
data = {"purchase_id": 4, "S_ID": 1,"S_totalPrice":222,"S_time":""}
insert_data(table_name, data)
