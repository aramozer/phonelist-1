# import sqlite3
# conn = sqlite3.connect("phone.db")
import psycopg2
conn = psycopg2.connect(
    host="localhost",
    database="phone",
    user="phone",
    password="abc123"
)


def read_phonelist(C):
    cur = C.cursor()
    cur.execute("SELECT * FROM phonelist;")
    rows = cur.fetchall()
    cur.close()
    return rows
def add_phone(C, name, phone, address):
    cur = C.cursor()
    cur.execute(f"INSERT INTO phonelist VALUES ('{name}', '{phone}', '{address}');")
    cur.close()
def delete_phone(C, name):
    cur = C.cursor()
    cur.execute(f"DELETE FROM phonelist WHERE name = '{name}';")
    cur.close()
def save_phonelist(C):
    cur = C.cursor()
    try:
        cur.execute("COMMIT;")
        print("Phonelist saved!")
    except:
        print("No changes!")
    cur.close()

list_of_inst = ('''Hello and welcome to the phone list, available commands:
add - add a phone number
delete - delete a contact
list - list all phone numbers
save - save the list
help - for list of commands
quit - quit the program''')

print(list_of_inst)

while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ").upper()
    if cmd == "LIST":
        print(read_phonelist(conn))
    elif cmd == "ADD":
        name = input("  Name: ")
        phone = input("  Phone: ")
        address = input(" Address ")
        add_phone(conn, name, phone, address)
    elif cmd == "DELETE":
        name = input("  Name: ")
        delete_phone(conn, name)
    elif cmd == "SAVE":
        save_phonelist(conn)
    elif cmd == "HELP":
        print(list_of_inst)
        save_phonelist(conn)
    elif cmd == "QUIT":
        save_phonelist(conn)
        exit()
    else:
        print("Unknown command:", cmd)


    
