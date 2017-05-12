class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0:
            return
        wd.find_element_by_link_text("groups").click()

    def open_home_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/index.php") and len(wd.find_elements_by_name("add")) > 0:
            return
        wd.get("http://localhost/addressbook/index.php")

    def return_group_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0:
            return
        wd.find_element_by_link_text("group page").click()

    def return_home_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/index.php") and len(wd.find_elements_by_name("add")) > 0:
            return
        wd.find_element_by_link_text("home").click()