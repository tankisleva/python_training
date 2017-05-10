from model.contact import Contact

    
def test_add_contact(app):
    app.contact.create(Contact(firstname="Oleg", lastname="Malyshev", nickname="tanki_sleva1", mobilephone="+79264789566"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", lastname="", nickname="",
                       mobilephone="+79264789566"))





