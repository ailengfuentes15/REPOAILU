from src.pages.BasePage import BasePage
from selenium.webdriver.common.by import By

import logging

class CartPage(BasePage):

    add_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_agregado = (By.CSS_SELECTOR, ".shopping_cart_badge")
    go_cart = (By.XPATH, "//a[@class='shopping_cart_link']")
    bag_cart = (By.XPATH, "//div[normalize-space()='Sauce Labs Backpack']")
    checkout_button = (By.ID, "checkout")


    def add_products_cart (self):
        self.click_element(self.add_cart_button)

    def verify_contador_cart (self):
        self.click_element(self.cart_agregado)

    def verify_navigate_cart (self):
        self.click_element(self.go_cart)

    def go_to_cart_page(self):
        self.click_element(self.go_cart)
    
    def click_checkout_button(self):
        self.click_element(self.checkout_button)

    def cart_completo(self):
        self.add_products_cart()
        self.go_to_cart_page()
        self.click_checkout_button()
       