import psycopg2

connect_info="dbname='testDatabase' user='postgres' password='password' host='localhost' port='5432'"

def create_table():
    conn=psycopg2.connect(connect_info)
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn=psycopg2.connect(connect_info)
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)",(item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn=psycopg2.connect(connect_info)
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn=psycopg2.connect(connect_info)
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn=psycopg2.connect(connect_info)
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()

#create_table()
#insert("Wine Glass", "8", "10.50")
#insert("Water Glass", "10", "2.50")
#insert("Coffee Cup", "5", "5.35")


#delete('Coffee Cup')

#update(11,6.50, "Water Glass")

print(view())
