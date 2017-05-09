from model.contact import Contact


def test_modify_contact(app):
    app.session.login(user="admin", password="secret")
    app.contact.modify(
        Contact(firstname="Oleg", lastname="Malyshev", nickname="tanki_sleva1", mobilephone="+79264789566"))
    app.session.logout()