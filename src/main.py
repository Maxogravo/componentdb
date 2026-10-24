import sqlite3

action = ""
connection = sqlite3.connect("src/database.db")
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS components (
        component id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        desc TEXT,
        value TEXT,
        quantity INTEGER)
    """)

def  add_component(name, desc, value, quantity):
    cursor.execute("INSERT INTO components (name, desc, value, quantity) VALUES (?,?,?,?)", (name, desc, value, quantity))
    connection.commit()

def list_components():
    cursor.execute("SELECT * FROM components")
    return cursor.fetchall()


while action != "bye":
    action = input("Enter action (add/list/bye): ")
    if action == "add":
        name = input("Enter component name: ")
        desc = input("enter component description: ")
        value  =  input("Enter component value: ")
        quantity = int(input("Enter component quantity: "))
        add_component(name,desc,value,quantity)

    elif action == "list":
        lscomponents = list_components()
        for component in lscomponents:
            print(f"ID: {component[0]}, Name: {component[1]}, Description: {component[2]}, Value: {component[3]}, Quantity: {component[4]}")

connection.close()