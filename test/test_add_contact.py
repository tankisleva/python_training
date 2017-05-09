import pytest

from fixture.Application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_contact(app):
    app.session.login(user="admin", password="secret")
    app.contact.create(Contact(firstname="Oleg", lastname="Malyshev", nickname="tanki_sleva1", mobilephone="+79264789566"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(user="admin", password="secret")
    app.contact.create(Contact(firstname="", lastname="", nickname="",
                       mobilephone="+79264789566"))
    app.session.logout()




