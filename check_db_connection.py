# import mysql.connector
#import pymysql.cursors

from model.group import Group

#from fixture.db import DbFixture
from fixture.orm import ORMFixture

# connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")
db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
#connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

# try:
#     groups = db.get_group_list()
#     for group in groups:
#         print(group)
#     print(len(groups))
# finally:
#     db.destroy()


# try:
#     l = db.get_contacts_in_group(Group(id="35"))
#     for item in l:
#         print(item)
#     print(len(l))
# finally:
#     pass #db.destroy()

try:
    l = db.get_contacts_in_group(Group(id="35"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass #db.destroy()

