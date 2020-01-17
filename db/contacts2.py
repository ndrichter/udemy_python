import sqlite3

db = sqlite3.connect("contacts.sqlite")

new_email = 'update@update.com'
name = input("Please enter a name: ")

update_sql = "UPDATE contacts SET email = ? WHERE name = ?"

update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, name))  # prevent sql injection

print("{} rows updated".format(update_cursor.rowcount))

update_cursor.connection.commit()
update_cursor.close()

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name, phone, email)
    print("-" * 20)

db.close()
