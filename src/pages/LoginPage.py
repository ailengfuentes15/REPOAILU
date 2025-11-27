from src.pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    username = (By.ID, "user-name")
    password = (By.ID, "password") 
    login_button = (By.ID, "login-button")
    product_selector = (By.XPATH, "//span[@class='title']")

    login_data = "login.json"

    def open_url(self):
        get_url = self.get_data(self.login_data) #LEE EL ARCHIVO JSON
        url_value = get_url["url"] #DECLARO UNA VARIABLE "VALUE"PARA DECIRLE, DEL JSON QUIERO QUE BUSQUES LA "URL"----> DE DONDE? DE LA VARIABLEGET URL CREADA ANTERIORMENTE
        self.navigate_to(url_value)

    def get_url(self):
        get_url = self.get_data(self.login_data)  # LEE EL ARCHIVO JSON
        url_value = get_url["url"]


    def enter_username(self):
        get_username = self.get_data(self.login_data)
        username_value = get_username["username"]
        self.input_text(self.username, username_value)

    def enter_invalid_username(self):
        get_invalid_username = self.get_data(self.login_data)
        invalid_username_value = get_invalid_username["user_locked"]
        self.input_text(self.username, invalid_username_value)

    def enter_password(self):
        get_password = self.get_data(self.login_data)
        password_value = get_password["password"]
        self.input_text(self.password, password_value)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def login_completo(self):
        self.open_url()
        self.enter_username()
        self.enter_password()
        self.click_login_button()