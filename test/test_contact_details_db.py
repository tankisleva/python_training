from model.contact import Contact


def test_deatails_on_contact_tabe(app, db):
   contact_from_table_list = app.contact.get_contact_list_all_data_from_table()
   contact_list_db = db.get_contact_list_alt_data()
   assert sorted(contact_from_table_list, key=Contact.id_or_max) == sorted(contact_list_db, key=Contact.id_or_max)





