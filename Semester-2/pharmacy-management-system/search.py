import sqlite3

def search_in_mid(letters):
    try:
        searchBy="M_name"
        table="Medicine"

        conn = sqlite3.connect('pharma.db')
        cur = conn.cursor()

        cur.execute(f"SELECT * FROM {table} WHERE {searchBy} LIKE ?", (letters + '%',))
        results = cur.fetchall()

        return results
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return []
    finally:
        if conn:
            conn.close()







letters= 'Abimol'
print(search_in_mid(letters))