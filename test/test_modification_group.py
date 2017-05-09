from model.group import Group


def test_modify_group(app):
    app.session.login(user="admin", password="secret")
    app.group.modify_first(Group(name="testname", header="testheader", footer="testfooter"))
    app.session.logout()