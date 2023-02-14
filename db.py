from requests_html import HTMLSession
from bs4 import BeautifulSoup
import sqlite3

url = "https://www.jessops.com/drones?fh_start_index=21&fh_view_size=21"
r = HTMLSession()


conn = sqlite3.connect("jessop.db")
c = conn.cursor()

c.execute("""CREATE TABLE drones(name TEXT,link TEXT, price INT)""")


page = r.get(url)
soup = BeautifulSoup(page.content, "html.parser")

items = soup.find_all("div", {"class": "f-grid prod-row"})
for item in items:
    name = item.find("h4").find("a").text
    url = "https://www.jessops.com" + str(item.find("h4").find("a")["href"])
    price = item.find("p", {"class": "price larger"}).text.strip().replace("£", "")
    c.execute("""INSERT INTO drones VALUES(?,?,?)""", (name, url, price))
    c.commit()


# import sqlite3


# conn = sqlite3.connect("lunch.db")
# c = conn.cursor()

# # c.execute("""CREATE TABLE meals(sandwich TEXT, fruit TEXT, tablenumber INT)""")


# sandwich = "cheese"
# fruit = "banana"
# tablenumber = 21

# c.execute("""INSERT INTO meals VALUES(?,?,?)""", (sandwich, fruit, tablenumber))
# conn.commit()

# c.execute("""SELECT fruit FROM meals""")
# results = c.fetchall()
# print(results)
