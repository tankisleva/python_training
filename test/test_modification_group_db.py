from model.group import Group
import random


#модификация группы с проверкой через бд
def test_modify_group_db(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    groupedit = random.choice(old_groups)
    group = Group(id=groupedit.id, name="testname", header="testheader", footer="testfooter")
    app.group.modify_group_by_id(group, groupedit.id)
    new_groups = db.get_group_list()
    old_groups.remove(groupedit)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)