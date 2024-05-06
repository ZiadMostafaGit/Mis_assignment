from datetime import datetime, timedelta
import sqlite3

def fetch_near_expired_medicines():
    conn = sqlite3.connect('pharma.db')
    cur = conn.cursor()
    try:
        # Calculate the expiration date two months from now
        current_date = datetime.now()
        expiration_date = (current_date + timedelta(days=60)).replace(day=1)  # Set day to 1 to ignore days in comparison
        # Fetch near-expired medicines
        cur.execute("SELECT M_Name, Quantity, Expire_Date FROM Medicine")
        all_medicines = cur.fetchall()
        near_expired_medicines = []
        for medicine in all_medicines:
            expire_month, expire_year = map(int, medicine[2].split('/'))
            expire_date = datetime(expire_year, expire_month, 1)  # Set day to 1 for comparison
            if expire_date <= expiration_date:
                near_expired_medicines.append(medicine)
        return near_expired_medicines
    except sqlite3.Error as e:
        print("Error fetching near-expired medicines:", e)
        return []
    finally:
        conn.close()
