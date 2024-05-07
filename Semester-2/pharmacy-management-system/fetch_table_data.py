import sqlite3

#دي فانكشن تديها اسم الجدول ترجعلك كل الداتا اللي جواه
def fetch_table_data(table):
    conn = sqlite3.connect('pharma.db')
    cur = conn.cursor()
    try:
        cur.execute(f"SELECT rowid, * FROM {table}")
        rows = cur.fetchall()
        fetched_data = []

        if rows:
            for row in rows:
                if len(row) == 2:
                    fetched_data.append((row[1]))
                if len(row) == 3:
                    fetched_data.append((row[1],row[2]))
                elif len(row) == 4:
                    fetched_data.append((row[1],row[2],row[3]))
                elif len(row) == 5:
                    fetched_data.append((row[1],row[2],row[3],row[4]))
                elif len(row) == 6:
                    fetched_data.append((row[1],row[2],row[3],row[4],row[5]))
                elif len(row) == 7:
                    fetched_data.append((row[1],row[2],row[3],row[4],row[5],row[6]))
                elif len(row) == 8:
                    fetched_data.append((row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
        else:
            fetched_data.append(("No data found."))
        return fetched_data

    except sqlite3.Error as e:
        return [(f"Error occurred:", e)]


    finally:
        conn.close()

# table="customer"
# x = fetch_table_data(table)
# print(x)
