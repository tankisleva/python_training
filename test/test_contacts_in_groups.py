from model.contact import Contact
from model.group import Group
import random


def test_add_contact_in_groups(app):
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Oleg", lastname="Malyshev"))
    old_contacts = db.get_contact_list()
    old_groups = db.get_group_list()
    contact = random.choice(old_contacts)
    group = random.choice(old_groups)
    contacts_in_group_old = db.get_contacts_in_group(group)
    if contacts_in_group_old.contains(contact.id):
        app.contact.delete_contact_in_bgroup(contact, group)
    app.contact.add_contact_in_bgroup(contact, group)
    contacts_in_group_new = db.get_contacts_in_group(group)
    contacts_in_group_old.append(contact)
    assert sorted(contacts_in_group_old, key=Contact.id_or_max) == sorted(contacts_in_group_new, key=Contact.id_or_max)

