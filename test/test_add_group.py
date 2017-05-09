from model.group import Group


def test_add_group(app):
    app.session.login(user="admin", password="secret")
    app.group.create(Group(name="testname", header="testheader", footer="testfooter"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(user="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()



