import mysql.connector
from model.group import Group
from model.contact import Contact
import re


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def get_contact_list_all_data(self):
        def clear(s):
            return re.sub("[() -]", "", s)

        def clear_email_phones(s):
            return re.sub("\n+", "\n", s)
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, email, email2, email3 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, email, email2, email3) = row
                phones = clear(home) + "\n" + clear(mobile) + "\n" + clear(
                    work)
                emails = email + "\n" + email2 + "\n" + email3
                phones = clear_email_phones(phones).strip("\n")
                emails = clear_email_phones(emails).strip("\n")
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address, allemails=emails, allphones=phones))
        finally:
            cursor.close()
        return list

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
