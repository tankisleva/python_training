from model.contact import Contact

    
def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Oleg", lastname="Malyshev", nickname="tanki_sleva1", mobilephone="+79264789566")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_add_contact_firstname(app):
#     app.contact.create(Contact(firstname="Oleg"))


# def test_add_empty_contact(app):
#     app.contact.create(Contact(firstname="", lastname="", nickname="",
#                        mobilephone="+79264789566"))





