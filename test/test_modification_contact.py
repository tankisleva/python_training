from model.contact import Contact


def test_modify_contact(app):
    app.contact.modify(
        Contact(firstname="Oleg", lastname="Malyshev", nickname="tanki_sleva1", mobilephone="+79264789566"))