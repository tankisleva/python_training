from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Dima"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Oleg", lastname="Malyshev", nickname="tanki_sleva1", mobilephone="+79264789566")
    contact.id = old_contacts[0].id
    app.contact.modify(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
