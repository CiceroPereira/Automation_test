from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

CEP_INPUT_FIELD = (By.ID, 'campoCEP')
ADDRESS_TABLE_RESULTS = ('div[id="resultado"] > table > tbody >'
                        ' tr:nth-child(%s) > td:nth-child(2)')
SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'center > font')
SEARCH_BUTTON = (By.CSS_SELECTOR, 'input[type="button"]')
RESULTS_LABLE = (By.CSS_SELECTOR, 'div > center > strong')
address_fields_position = {
    "public_area_type": "1",
    "public_area": "2",
    "neighborhood": "3",
    "city": "4",
    "uf": "5"
}

class FindCepPage(BasePage):

    def type_in_cep_field(self, cep):
        super().type_in(CEP_INPUT_FIELD, cep)

    def click_on_search_button(self):
        super().click(SEARCH_BUTTON)

    def get_success_message(self):
        super().wait(EC.visibility_of_element_located(RESULTS_LABLE))
        return super().find(SUCCESS_MESSAGE).text

    def get_public_area_type_value(self):
        position = address_fields_position['public_area_type']
        element = (By.CSS_SELECTOR, ADDRESS_TABLE_RESULTS % position)
        return super().find(element).text

    def get_public_area_value(self):
        position = address_fields_position['public_area']
        element = (By.CSS_SELECTOR, ADDRESS_TABLE_RESULTS % position)
        return super().find(element).text

    def get_neighborhood_value(self):
        position = address_fields_position['neighborhood']
        element = (By.CSS_SELECTOR, ADDRESS_TABLE_RESULTS % position)
        return super().find(element).text

    def get_city_value(self):
        position = address_fields_position['city']
        element = (By.CSS_SELECTOR, ADDRESS_TABLE_RESULTS % position)
        return super().find(element).text

    def get_uf_value(self):
        position = address_fields_position['uf']
        element = (By.CSS_SELECTOR, ADDRESS_TABLE_RESULTS % position)
        return super().find(element).text
