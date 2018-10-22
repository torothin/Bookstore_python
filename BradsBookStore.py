#Brad Duvall
#Book Store App V1 (Attempt to complete prior to performing exercise)
#1/25/17 to 2/6/17 (Estimated 30-40 hours to complete)
#Uses SQLite3 and Tkinter to create an executable bookstore app
#

from tkinter import *
import sqlite3

window=Tk()
window.resizable(0,0)

#Creates the initial database and database table
def create_table():
    conn=sqlite3.connect("Bradsbookstore.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (position INTEGER, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

#Adds and entry into the bookstore database
def insert():
    conn=sqlite3.connect("Bradsbookstore.db")
    cur=conn.cursor()
    position=max_position()+1
    title=e1_value.get()
    author=e2_value.get()
    year=int(e3_value.get())
    isbn=int(e4_value.get())
    cur.execute("INSERT INTO store VALUES(?,?,?,?,?)",(position,title,author,year,isbn))
    conn.commit()
    conn.close()
    view()

#Finds the largest value for position.  Called by insert()
def max_position():
    conn=sqlite3.connect("Bradsbookstore.db")
    cur=conn.cursor()
    cur.execute("SELECT MAX(position) FROM store")
    max_position_value=cur.fetchone()[0]
    conn.close()
    return max_position_value

#used only for initial library building
def insert2(position,title,author,year,isbn):
    conn=sqlite3.connect("Bradsbookstore.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?,?,?)",(position,title,author,year,isbn))
    conn.commit()
    conn.close()
    view()

#Grabs and inserts all the books stored in the database.
#Also updates position (book number) to ensure continuity for the position values
def view():
    conn=sqlite3.connect("Bradsbookstore.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    i=1
    for rows in cur.fetchall():
        cur.execute("UPDATE store SET position=? WHERE isbn=?",(i,rows[4]))
        i+=1
    cur.execute("SELECT * FROM store")
    text_window.delete(0,END)
    for item in cur.fetchall():
        text_window.insert(END,item)
    conn.commit()
    conn.close()

#deletes a book entry based on Listbox selection
def delete():
    conn=sqlite3.connect("Bradsbookstore.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE position=?",(text_window.get(ACTIVE)[0],))
    conn.commit()
    conn.close()
    view()

#Function to update information for a book stored in the database based on Listbox selection
def update():
    conn=sqlite3.connect("Bradsbookstore.db")
    cur=conn.cursor()
    if e1_value.get()=="":
        update_title=cur.execute("SELECT title FROM store WHERE position=?",(text_window.get(ACTIVE)[0],)).fetchone()[0]
    else:
        update_title=e1_value.get()
    if e2_value.get()=="":
        update_author=cur.execute("SELECT author FROM store WHERE position=?",(text_window.get(ACTIVE)[0],)).fetchone()[0]
    else:
        update_author=e2_value.get()
    if e3_value.get()=="":
        update_year=cur.execute("SELECT year FROM store WHERE position=?",(text_window.get(ACTIVE)[0],)).fetchone()[0]
    else:
        update_year=e3_value.get()
    if e4_value.get()=="":
        update_isbn=cur.execute("SELECT isbn FROM store WHERE position=?",(text_window.get(ACTIVE)[0],)).fetchone()[0]
    else:
        update_isbn=e4_value.get()
    cur.execute("UPDATE store SET title=?, author=?, year=?, isbn=? WHERE position=?", (update_title,update_author,update_year,update_isbn,text_window.get(ACTIVE)[0]))
    conn.commit()
    conn.close()
    view()

#performs a search on one entry only, multiple entries will be prioritized by entry position (Title, Author,Year, or ISBN)
def search():
    conn=sqlite3.connect("Bradsbookstore.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    text_window.delete(0,END)
    if e1_value.get()!="":
        for rows in cur.fetchall():
            if e1_value.get()==rows[1]:
                text_window.insert(END,rows)
    elif e2_value.get()!="":
        for rows in cur.fetchall():
            if e2_value.get()==rows[2]:
                text_window.insert(END,rows)
    elif e3_value.get()!="":
        for rows in cur.fetchall():
            if int(e3_value.get())==rows[3]:
                text_window.insert(END,rows)
    elif e4_value.get()!="":
        for rows in cur.fetchall():
            if int(e4_value.get())==rows[4]:
                text_window.insert(END,rows)
    conn.close()



create_table()


#inputs
l1=Label(window, text="Title")
l1.grid(row=0, column=0)

e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

l2=Label(window, justify="right", text="Author")
l2.grid(row=0, column=2)

e2_value=StringVar()
e2=Entry(window, textvariable=e2_value)
e2.grid(row=0, column=3)

l3=Label(window,text="Year")
l3.grid(row=1, column=0)

e3_value=StringVar()
e3=Entry(window, textvariable=e3_value)
e3.grid(row=1, column=1)

l4=Label(window,text="ISBN")
l4.grid(row=1, column=2)

e4_value=StringVar()
e4=Entry(window, textvariable=e4_value)
e4.grid(row=1, column=3)


#command buttons
b1=Button(window, text="View All", command=view, width=15)
b1.grid(row=2, column=5)

b2=Button(window, text="Search Entry", command=search, width=15)
b2.grid(row=3, column=5)

b3=Button(window, text="Add Entry", command=insert, width=15)
b3.grid(row=4, column=5)

b4=Button(window, text="Update Selected", command=update, width=15)
b4.grid(row=5, column=5)

b5=Button(window, text="Delete Selected", command=delete, width=15)
b5.grid(row=6, column=5)

b6=Button(window, text="Close", command=quit, width=15)
b6.grid(row=7, column=5)

#Text Box
scroll_bar=Scrollbar(window, orient="vertical")
text_window=Listbox(window, yscrollcommand=scroll_bar.set,height=10, width=60)
text_window.grid(row=2,column=0, rowspan=6, columnspan=4)
scroll_bar.config(command=text_window.yview)
scroll_bar.grid(row=2,column=4,rowspan=6,sticky="NS")

# #Initial database build
# insert2(1,"The Stand","Steven King","2012","0307947300")
# insert2(2,"IT","Steven King","2016","1501142976")
# insert2(3,"Dark Tower","Steven King","2016","1501143514")
# insert2(4,"Heart of Atlantas","Steven King","2000","0671024248")
# insert2(5,"What You Break","Reed Farrel Coleman","2017","0399173048")
# insert2(6,"A Separation: A Novel","Katie Kitamura","2017","0399576101")
# insert2(7,"A Piece of the World: A Novel","Christina Baker Kline","2017","0062356267")
# insert2(8,"1984","George Orwell","1950","0451524934")
# insert2(9,"Fahrenheit 451","Ray Bradbury","2012","1451673310")
# insert2(10,"Catch-22: 50th Anniversary Edition","Joseph Heller","2011","1451626657")
# insert2(11,"The Catcher in the Rye","J.D. Salinger","1991","0316769487")
# insert2(12,"Of Mice and Men","John Steinbeck","1991","0140177396")


view()

window.mainloop()
