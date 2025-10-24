from src.pages.BasePage import BasePage
from selenium.webdriver.common.by import By

import logging

class InventoryPage(BasePage):

    product_selector = (By.XPATH, "//span[@class='title']")
    bag_selector = (By.XPATH, "//div[normalize-space()='Sauce Labs Backpack']")
    bike_selector = (By.XPATH, "//div[normalize-space()='Sauce Labs Bike Light']")
    menu_burger = (By.ID, "react-burger-menu-btn")
    filter_selector = (By.XPATH , "//select[@class='product_sort_container']")
    cart_selector = (By.XPATH, "//a[@class='shopping_cart_link']")


    def is_element_present(self, selector):
        try:
            self.wait_for_element(selector)
            logging.info(f"Elemento presente: {selector}")
            return True
        except Exception as e:
            logging.error(f"Elemento NO presente: {selector}. Error: {e}")
            return False

    def is_element_visible(self, selector):
        try:
            element = self.wait_until_visible(selector)
            visible = element.is_displayed()
            if visible:
                logging.info(f"Elemento visible: {selector}")
            else:
                logging.warning(f"Elemento encontrado pero NO visible: {selector}")
            return visible
        except Exception as e:
            logging.error(f"Error verificando visibilidad de {selector}: {e}")
            return False
