from sys import maxsize

class Contact:

    def __init__(self, firstname=None, lastname=None, nickname=None, mobilephone=None,id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.mobilephone = mobilephone
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.firstname, self.lastname, self.nickname, self.id)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and \
               self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

