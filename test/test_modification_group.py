from model.group import Group


def test_modify_group(app):
    app.group.modify_first(Group(name="testname", header="testheader", footer="testfooter"))