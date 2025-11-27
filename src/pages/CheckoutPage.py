from src.pages.BasePage import BasePage
from selenium.webdriver.common.by import By

import logging

class CheckoutPage(BasePage):

    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    finish_button = (By.ID, "finish")
    complete_order = (By.XPATH, "//h2[normalize-space()='Thank you for your order!']")

    checkout_data = "checkout.json"


    def enter_first_name(self):
        get_first_name = self.get_data(self.checkout_data)
        first_name_value = get_first_name["first_name"]
        self.input_text(self.first_name, first_name_value)

    def enter_last_name(self):
        get_last_name = self.get_data(self.checkout_data)
        last_name_value = get_last_name["last_name"]
        self.input_text(self.last_name, last_name_value)

    def enter_postal_code(self):
        get_postal_code = self.get_data(self.checkout_data)
        postal_code_value = get_postal_code["postal_code"]
        self.input_text(self.postal_code, postal_code_value)
        

    def click_continue_button(self):
        self.click_element(self.continue_button)

    def click_finish_button(self):
        self.click_element(self.finish_button)

    def get_checkout_complete_text(self):
        return self.get_text(self.checkout_complete)