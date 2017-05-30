from model.contact import Contact
import random


#модификация контакта с проверкой через бд
def test_modify_contact_db(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Oleg", lastname="Malyshev"))
    old_contacts = db.get_contact_list()
    contactedit = random.choice(old_contacts)
    contact = Contact(id=contactedit.id, firstname="Oleg", lastname="Malyshev")
    app.contact.modify_by_id(contact, contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contactedit)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)