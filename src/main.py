import sqlite3

action = ""
connection = sqlite3.connect("src/database.db")
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS components (
        component_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        desc TEXT,
        value TEXT,
        quantity INTEGER)
    """)

def  add_component():
    name = input("Enter component name: ")
    desc = input("Enter component description: ")
    value = input("Enter component value: ")
    quantity = int(input("Enter component quantity: "))
    cursor.execute("INSERT INTO components (name, desc, value, quantity) VALUES (?,?,?,?)", (name, desc, value, quantity))
    connection.commit()

def replenish_component(id, quantity):
    cursor.execute("UPDATE components SET quantity = quantity + ? WHERE component_id = ?", (quantity, id))
    connection.commit()

def remove_component(id, quantity):
    cursor.execute("UPDATE components SET quantity = quantity - ? WHERE component_id = ?", (quantity, id))
    connection.commit()

def list_components(all):
    if all == True:
        cursor.execute("SELECT * FROM components")
    else:
        cursor.execute("SELECT * FROM components WHERE quantity > 0")
    return cursor.fetchall()


while action != "bye":
    action = input("Enter action (add/remove/list/bye): ")

    match action:
        case "add":
            print("1. Add a new component")
            print("2. Add an existing component")
            sub_action = input("Enter sub-action (1/2): ")
            if sub_action == "1":
                add_component()
            elif sub_action == "2":
                components = list_components(True)
                for component in components:
                    print(component)
                id = int(input("Enter component id to replenish: "))
                quantity = int(input("Enter quantity to add: "))
                replenish_component(id, quantity)

        case "remove":
            id = int(input("Enter component id to remove: "))
            quantity = int(input("Enter quantity to remove: "))
            remove_component(id, quantity)

        case "list":
            components = list_components(False)
            for component in components:
                print(component)

        case "bye":
            print("Goodbye!")
            
        case _:
            print("Invalid action. Please try again.")

connection.close()