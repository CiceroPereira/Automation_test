from pages.BasePage import BasePage


class HomeActions(BasePage):
 
    def open_application (self, url):
        super().open_url(url)
