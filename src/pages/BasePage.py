from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import json
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import logging
from selenium.webdriver.common.keys import Keys

# Configuración básica del logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class BasePage:

    def __init__(self, driver):
        """Inicializa la clase BasePage con una instancia de WebDriver."""
        self.driver = driver

    @staticmethod
    def initialize_ChromeDriver():
        options = Options()

        # Desactiva popups de Google Chrome (incluye guardar contraseña y alertas de contraseñas filtradas)
        options.add_argument("--disable-features=PasswordManagerEnabled,AutofillServerCommunication")
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_setting_values.notifications": 2,
            "profile.default_content_setting_values.popups": 0
        })

        # Modo estable si tenés popups molestos de Chrome
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")

        driver = webdriver.Chrome(options=options)
        return driver



    @staticmethod
    def initialize_ChromeDriver_headless(headless=True):
        """Inicializa y retorna una nueva instancia de Chrome WebDriver en modo headless si se indica."""
        options = Options()
        if headless:
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
        return driver

    def max_window(self):
        """Maximiza la ventana del navegador."""
        self.driver.maximize_window()

    def close_browser(self):
        """Cierra el navegador y finaliza la sesión del WebDriver."""
        self.driver.quit()

    def navigate_to(self, url):
        """Navega a la URL especificada en el navegador."""
        self.driver.get(url)

    def wait_for_element(self, web_elements, timeout=30):
        """
        Espera hasta que el elemento especificado esté presente en el DOM.
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(web_elements))

    def wait_until_visible(self, web_elements, timeout=30):
        """
        Espera hasta que el elemento especificado esté presente en el DOM.
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(web_elements))

    def wait_until_clickable(self, web_elements, timeout=30):
        """Espera hasta que el elemento sea clickeable."""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(web_elements))

    def click_element(self, web_elements):
        """Espera a que el elemento esté presente y clickeable, luego hace clic."""
        logging.info(f"Haciendo click en el elemento con localizador: {web_elements}")
        self.wait_for_element(web_elements)
        element = self.wait_until_clickable(web_elements)
        element.click()
        logging.info(f"Click realizado en el elemento: {web_elements}")

    def input_text(self, web_elements, text):
        """
        Espera a que el elemento esté presente y clickeable, luego escribe el texto proporcionado en él.
        """
        self.wait_for_element(web_elements)
        element = self.wait_until_clickable(web_elements)
        element.clear()
        logging.info(f"Ingresando texto en el elemento: {web_elements}")
        element.send_keys(text)
        logging.info(f"Texto '{text}' ingresado en el elemento: {web_elements}")

    def get_text(self, web_elements):
        """Obtiene el texto de un elemento web después de esperar su presencia."""
        logging.info(f"Obteniendo texto del elemento con localizador: {web_elements}")
        element = self.wait_for_element(web_elements)
        text = element.text
        logging.info(f"Texto obtenido del elemento {web_elements}: '{text}'")
        return text

    def get_url(self):
        """Devuelve la URL actual del navegador."""
        current_url = self.driver.current_url
        logging.info(f"URL actual: {current_url}")
        return current_url

    @staticmethod
    def get_data(filename):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(base_dir, '..', 'Testdata')
        abs_path = os.path.join(data_dir, filename)
        with open(abs_path, 'r') as archive:
            return json.load(archive)

    def hover_element_and_click(self, hover_locator):
        """
        Realiza un hover sobre un elemento y luego hace clic en él.


        Args:
            hover_locator: Tupla (By, value) del elemento sobre el que se hace hover.
        """
        logging.info(f"Realizando hover sobre el elemento con localizador: {hover_locator}")
        hover_element = self.wait_for_element(hover_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(hover_element).perform()
        logging.info(f"Hover realizado sobre el elemento: {hover_locator}")
        logging.info(f"Haciendo clic en el elemento después del hover: {hover_locator}")
        hover_element.click()

    def select_dropdown(self, web_elements):
        element = self.wait_for_element(web_elements)
        element.send_keys(Keys.DOWN, Keys.ENTER)

        # Pone el foco en una nueva ventana

    def switch_to_new_window(self):
        WebDriverWait(self.driver, 10).until(lambda driver: len(driver.window_handles) > 1)
        nueva_ventana = self.driver.window_handles[1]
        self.driver.switch_to.window(nueva_ventana)


