from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

test_data = [
    Contact(firstname=random_string("firestname", 10), lastname=random_string("lastname", 20), address=random_string("address", 20)),
    Contact(firstname="", lastname="", address="")
]


test_data_random = [
    Contact(firstname=firstname, lastname=lastname, address=address)
    for firstname in ["", random_string("firstname", 10)]
    for lastname in ["", random_string("lastname", 20)]
    for address in ["", random_string("address", 20)]
]

test_data_five_group = [Contact(firstname="", lastname="", address="")] + [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 20), address=random_string("address", 20))
    for i in range(5)
]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)







