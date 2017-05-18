from model.contact import Contact

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        self.init_contact_creation()
        self.fill_contact_form(contact)
        self.submit_contact_creation()
        self.app.navigation.return_home_page()

    def modify(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()

    def type(self, filed_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(filed_name).click()
            wd.find_element_by_name(filed_name).clear()
            wd.find_element_by_name(filed_name).send_keys(text)

    def fill_contact_form(self, contact):
        self.type("firstname", contact.firstname)
        self.type("lastname", contact.lastname)
        self.type("nickname", contact.nickname)
        self.type("mobile", contact.mobilephone)

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.navigation.return_home_page()

    def submit_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def init_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def count(self):
        wd = self.app.wd
        self.app.navigation.return_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.app.navigation.return_home_page()
        table = wd.find_element_by_id("maintable")
        rows = table.find_elements_by_name("entry")
        contacts = []
        for row in rows:
            cells = row.find_elements_by_tag_name("td")
            firstname = cells[2].text
            lastname = cells[1].text
            id = cells[0].find_element_by_tag_name("input").get_attribute("value")
            contacts.append(Contact(firstname, lastname, id))

        return contacts




