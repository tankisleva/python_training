from model.contact import Contact

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        self.init_contact_creation()
        self.fill_contact_form(contact)
        self.submit_contact_creation()
        self.app.navigation.return_home_page()
        self.contact_cache = None

    def modify(self, contact, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

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
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.navigation.return_home_page()
        self.contact_cache = None

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

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.navigation.return_home_page()
            table = wd.find_element_by_id("maintable")
            rows = table.find_elements_by_name("entry")
            self.contact_cache = []
            for row in rows:
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                self.contact_cache.append(Contact(firstname, lastname, id))

        return list(self.contact_cache)




