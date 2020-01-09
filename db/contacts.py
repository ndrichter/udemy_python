import sqlite3

db = sqlite3.connect("contacts.sqlite")

db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts (name, phone, email) VALUES ('Nate', 5551234, 'nate@email.com')")
db.execute("INSERT INTO contacts VALUES ('Kelly', 5554321, 'kelly@email.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

# list
# print(cursor.fetchall())
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())  # produces None due to no more rows to fetch

# tuple
for name, phone, email in cursor:
    print(name, phone, email)
    print("-" * 20)
cursor.close()
db.commit()
db.close()
