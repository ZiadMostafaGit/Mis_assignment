import sqlite3

def delete(searchBy, table, letters):
    try:
        conn = sqlite3.connect('pharma.db')
        cur = conn.cursor()

        cur.execute(f"DELETE FROM {table} WHERE {searchBy} = ?", (letters))
        # No need to fetch results for DELETE statement
        conn.commit()  # Commit the deletion

        return True  # Return True to indicate success

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return False  # Return False to indicate failure

    finally:
        if conn:
            conn.close()

# Example usage
searchBy = "purchase_id"
table = "purchase"
letters = '2'
success = delete(searchBy, table, letters)
print("Deletion successful:", success)
