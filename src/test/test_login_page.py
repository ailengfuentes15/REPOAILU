
from src.pages.BasePage import BasePage
from src.pages.LoginPage import LoginPage
from selenium.webdriver.common.by import By
import pytest



class TestLogin:

    def test_login(self, driver):
        login_page = LoginPage(driver)
        login_page.login_completo()

        products_text = login_page.get_text(login_page.product_selector)

        assert "Products" in products_text, \
            f"Se esperaba 'Products' pero se obtuvo: {products_text}"

    

    @pytest.mark.smoke
    
    def test_login_invalid_username(self, driver):
        login_page = LoginPage(driver)     # <--- ESTA LÍNEA ES LA SOLUCIÓN
        login_page.open_url()
        login_page.enter_invalid_username()
        login_page.enter_password()
        login_page.click_login_button()

        error_message = login_page.get_text(
            (By.XPATH, "//h3[contains(text(),'Epic sadface')]")
        )

        assert "Sorry, this user has been locked out" in error_message
       
    