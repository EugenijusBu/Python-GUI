from sqlite3.dbapi2 import Row
from tkinter import *
import sqlite3



root = Tk()
root.geometry("360x500")

#databases


#create a databse or connect to one

conn = sqlite3.connect('address_book.db')

#creating a cursor
cur = conn.cursor()

#Create table
###
#cur.execute("""CREATE TABLE addresses(
 #       first_name text,
    #    last_name text,
     #   address text,
      #  city text,
       # state text,
     #   zipcode integer
        #)""")
###

def save_updates():
    #create a databse or connect to one
    conn = sqlite3.connect('address_book.db')
    #creating a cursor
    cur = conn.cursor()

    oid = delete_entry.get()
    #insert data into table
    cur.execute("""UPDATE addresses SET
    
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode
    
        WHERE oid = :oid""",
        {'first': f_name_editor.get(),
        'last' : l_name_editor.get(),
        'address':address_editor.get(),
        'city': city_editor.get(),           
        'state': state_editor.get(),
        'zipcode': zipcode_editor.get(),
        'oid': oid
        })

    #commit changes
    conn.commit()
    #close connection
    conn.close()

    editor.destroy()
    

def update():
    global editor
    editor = Tk()
    editor.geometry("360x500")


    #create a databse or connect to one
    conn = sqlite3.connect('address_book.db')
    #creating a cursor
    cur = conn.cursor()


    #creating global vars
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    #creating textboxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(column=1,row=0)
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(column=1,row=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(column=1,row=2)
    city_editor = Entry(editor, width=30)
    city_editor.grid(column=1,row=3)
    state_editor = Entry(editor, width=30)
    state_editor.grid(column=1,row=4)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(column=1,row=5)
    #creating textbox labels
    f_name_label = Label(editor,text="First Name")
    l_name_label = Label(editor,text="Last Name")
    address_label = Label(editor,text="Address")
    city_label = Label(editor,text="City")
    state_label = Label(editor,text="State")
    zipcode_label = Label(editor,text="Zipcode")
   
    f_name_label.grid(column=0,row=0)
    l_name_label.grid(column=0,row=1)
    address_label.grid(column=0,row=2)
    city_label.grid(column=0,row=3)
    state_label.grid(column=0,row=4)
    zipcode_label.grid(column=0,row=5)

    updatebtn = Button(editor, text="Update!", command=save_updates)
    updatebtn.grid(row=8, columnspan=2, column=0, padx=10, pady=10, ipadx=122)

    record_id = delete_entry.get()
    #query the database
    cur.execute("SELECT * FROM addresses WHERE oid=" + record_id)
    records = cur.fetchall()
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    #loop through results
    print_records = ""
    for record in records:
        print_records += str(record) +'\n'
    




    #commit changes
    conn.commit()
    #close connection
    conn.close()

def delete():
    conn = sqlite3.connect('address_book.db')
    #creating a cursor
    cur = conn.cursor()

    cur.execute("DELETE from addresses WHERE oid=" + delete_entry.get())

    delete_entry.delete(0, END)
    #commit changes
    conn.commit()
    #close connection
    conn.close()

def submit():
    #create a databse or connect to one
    conn = sqlite3.connect('address_book.db')
    #creating a cursor
    cur = conn.cursor()


    #insert data into table
    cur.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode )",
        {
            'f_name': f_name.get(),
            'l_name' : l_name.get(),
            'address': address.get(),
            'city': city.get(),
            'state': state.get(),
            'zipcode': zipcode.get()
        })

    #commit changes
    conn.commit()
    #close connection
    conn.close()


    #clearing textboxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

def query():
    #create a databse or connect to one
    conn = sqlite3.connect('address_book.db')
    #creating a cursor
    cur = conn.cursor()

    #query the database
    cur.execute("SELECT *, oid FROM addresses")
    records = cur.fetchall()
    #print(records)
    #loop trough results
    print_records = ""
    for record in records:
        print_records += str(record) +'\n'


    query_label = Label(root, text=print_records)
    query_label.grid(row=11,column=0, columnspan=2)



    #commit changes
    conn.commit()
    #close connection
    conn.close()

#creating textboxes
f_name = Entry(root, width=30)
f_name.grid(column=1,row=0)
l_name = Entry(root, width=30)
l_name.grid(column=1,row=1)
address = Entry(root, width=30)
address.grid(column=1,row=2)
city = Entry(root, width=30)
city.grid(column=1,row=3)
state = Entry(root, width=30)
state.grid(column=1,row=4)
zipcode = Entry(root, width=30)
zipcode.grid(column=1,row=5)
delete_entry = Entry(root, width=30)
delete_entry.grid(column=1,row=7)

#creating textbox labels
f_name_label = Label(root,text="First Name")
l_name_label = Label(root,text="Last Name")
address_label = Label(root,text="Address")
city_label = Label(root,text="City")
state_label = Label(root,text="State")
zipcode_label = Label(root,text="Zipcode")
delete_label = Label(root,text="SELECT OID")

f_name_label.grid(column=0,row=0)
l_name_label.grid(column=0,row=1)
address_label.grid(column=0,row=2)
city_label.grid(column=0,row=3)
state_label.grid(column=0,row=4)
zipcode_label.grid(column=0,row=5)
delete_label.grid(column=0,row=7)

#Create submit button
submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6,column=0,columnspan=2, pady=10,padx=10, ipadx=100)

#creating a query button
query_btn = Button(root, text="Show records", command=query)
query_btn.grid(row=10,columnspan=2,column=0, padx=10, pady=10, ipadx=129)

#creating a delete button
delete_btn = Button(root, text="Delete a record", command=delete)
delete_btn.grid(row=8,columnspan=2,column=0, padx=10, pady=10, ipadx=124)

#creating a update button
update_btn = Button(root, text="Update a record", command=update)
update_btn.grid(row=9,columnspan=2, column=0, padx=10, pady=10, ipadx=122)

#creating a button 

#commit changes
conn.commit()

#close connection
conn.close()


mainloop()