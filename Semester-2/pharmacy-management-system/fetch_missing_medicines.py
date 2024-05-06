import sqlite3

def fetch_missing_medicines():
    conn = sqlite3.connect('pharma.db')
    cur = conn.cursor()
    try:
        # Fetch medicines with quantity equal to 0
        cur.execute("SELECT M_Name, Quantity FROM Medicine WHERE Quantity = 0")
        missing_medicines = cur.fetchall()
        return missing_medicines
    except sqlite3.Error as e:
        print("Error fetching missing medicines:", e)
        return []
    finally:
        conn.close()
