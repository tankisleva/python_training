from sys import maxsize

class Contact:

    def __init__(self, firstname=None, lastname=None, nickname=None, homephone=None, mobilephone=None,
                 workphone=None, secondaryphone=None, address=None, email=None, email2=None, email3=None, id=None,
                 allemails=None, allphones=None):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.address = address
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.id = id
        self.allemails = allemails
        self.allphones = allphones

    def __repr__(self):
        return "%s:%s:%s" % (self.firstname, self.lastname, self.id)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and \
               self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

