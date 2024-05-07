import sqlite3

def fetch_table_data(table):
    conn = sqlite3.connect('pharma.db')
    cur = conn.cursor()
    try:
        cur.execute(f"PRAGMA table_info({table})")
        column_names = [column[1] for column in cur.fetchall()]

        cur.execute(f"SELECT * FROM {table}")
        rows = cur.fetchall()

        fetched_data = [dict(zip(column_names, row)) for row in rows]
        return fetched_data
    except sqlite3.Error as e:
        return [(f"Error occurred:", e)]
    finally:
        conn.close()

# table="Medicine"
# x = fetch_table_data(table)
# for i in range(10):
#     print(x[i])

# print(type(x))    
# # print(x)
