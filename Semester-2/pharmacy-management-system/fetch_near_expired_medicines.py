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
            expire_date_parts = medicine[2].split('/')
            if len(expire_date_parts) == 3:
                expire_date = datetime.strptime(medicine[2], '%d/%m/%Y')  # Parse the date string
            else:
                expire_date = datetime.strptime(medicine[2], '%m/%Y')  # Parse the date string without day
            if expire_date <= expiration_date:
                near_expired_medicines.append(medicine)
        return near_expired_medicines
    except sqlite3.Error as e:
        print("Error fetching near-expired medicines:", e)
        return []
    finally:
        conn.close()

# print(fetch_near_expired_medicines())
