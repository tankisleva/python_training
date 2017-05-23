import re

def test_deatails_on_contact_tabe(app):
   contact_from_edit_page = app.contact.get_contact_into_from_edit_page(0)
   contact_from_table_list = app.contact.get_contact_list_all_data_from_table()[0]

   firstname = contact_from_edit_page.firstname
   lastname = contact_from_edit_page.lastname
   address = contact_from_edit_page.address
   phones = [clear(contact_from_edit_page.homephone), clear(contact_from_edit_page.mobilephone), clear(contact_from_edit_page.workphone)]
   emails = [contact_from_edit_page.email, contact_from_edit_page.email2, contact_from_edit_page.email3]

   assert contact_from_table_list.firstname == firstname
   assert contact_from_table_list.lastname == lastname
   assert contact_from_table_list.address == address
   assert contact_from_table_list.allphones == phones
   assert contact_from_table_list.allemails == emails


def clear(s):
    return re.sub("[() -]", "", s)

