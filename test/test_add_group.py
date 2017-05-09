# -*- coding: utf-8 -*-
import pytest

from fixture.Application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(user="admin", password="secret")
    app.group.create(Group(name="testname", header="testheader", footer="testfooter"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(user="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()



