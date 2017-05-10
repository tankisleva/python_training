class GroupHelper:

    def __init__(self, app):
        self.app = app

    def submit_group_creation(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def create(self, new_group_data):
        self.app.navigation.open_group_page()
        self.init_group_creation()
        self.fill_group_form(new_group_data)
        self.submit_group_creation()
        self.app.navigation.return_group_page()

    def init_group_creation(self):
        wd = self.app.wd
        wd.find_element_by_name("new").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.app.navigation.open_group_page()
        self.select_first_group(wd)
        wd.find_element_by_name("delete").click()
        self.app.navigation.return_group_page()

    def modify_first(self, new_group_data):
        wd = self.app.wd
        self.app.navigation.open_group_page()
        self.select_first_group(wd)
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        wd.find_element_by_name("update").click()
        self.app.navigation.return_group_page()

    def type(self, filed_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(filed_name).click()
            wd.find_element_by_name(filed_name).clear()
            wd.find_element_by_name(filed_name).send_keys(text)

    def fill_group_form(self, group):
        self.type("group_name", group.name)
        self.type("group_header", group.header)
        self.type("group_footer", group.footer)

    def select_first_group(self, wd):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()





