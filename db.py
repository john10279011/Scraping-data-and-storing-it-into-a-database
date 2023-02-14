import sqlite3


conn = sqlite3.connect("lunch.db")
c = conn.cursor()

# c.execute("""CREATE TABLE meals(sandwich TEXT, fruit TEXT, tablenumber INT)""")


sandwich = "cheese"
fruit = "banana"
tablenumber = 21

# c.execute("""INSERT INTO meals VALUES(?,?,?)""", (sandwich, fruit, tablenumber))
# conn.commit()

c.execute("""SELECT fruit FROM meals""")
results = c.fetchall()
print(results)
