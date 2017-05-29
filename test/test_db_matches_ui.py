
from model.group import Group
from timeit import timeit


def test_group_list(app, db):
     print(timeit(lambda: app.group.get_group_list(), number=1))

     def clean(group):
         return Group(id=group.id, name=group.name.strip(), header=group.header.strip(), footer=group.footer.strip())
     print(timeit(lambda:map(clean, db.get_group_list()), number=2))
     assert False #assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)