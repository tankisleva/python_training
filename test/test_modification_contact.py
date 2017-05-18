from model.contact import Contact
from random import randrange


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Dima"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Oleg", lastname="Malyshev", nickname="tanki_sleva1", mobilephone="+79264789566")
    contact.id = old_contacts[index].id
    app.contact.modify(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
