from model.group import Group


def test_modify_group(app):
    app.group.modify_first(Group(name="testname", header="testheader", footer="testfooter"))


def test_modify_group_name(app):
    app.group.modify_first(Group(name="Olegggg"))