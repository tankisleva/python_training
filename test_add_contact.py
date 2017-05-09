
import pytest
from contact import Contact
from Application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_contact(app):
    app.login(user="admin", password="secret")
    app.create_contact(Contact(firstname="Oleg", lastname="Malyshev", nickname="tanki_sleva1", mobilephone="+79264789566"))
    app.logout()


def test_add_empty_contact(app):
    app.login( user="admin", password="secret")
    app.create_contact(Contact(firstname="", lastname="", nickname="",
                                           mobilephone="+79264789566"))
    app.logout()




