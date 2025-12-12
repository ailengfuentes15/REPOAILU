import pytest
import os
from datetime import datetime

# ------------------ API PAGES ------------------
from src.pages.peticiones.GetPage import GetPage
from src.pages.peticiones.PostPage import PostPage
from src.pages.peticiones.DeletePage import DeletePage

# ------------------ SELENIUM ------------------
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager




# =========================================================
# FIXTURES API
# =========================================================

@pytest.fixture(scope="session")
def base_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def get_page(base_url):
    return GetPage(base_url)


@pytest.fixture(scope="session")
def post_page(base_url):
    return PostPage(base_url)


@pytest.fixture(scope="session")
def delete_page(base_url):
    return DeletePage(base_url)


# =========================================================
# FIXTURE PARA SELENIUM (HEADLESS)
# =========================================================
@pytest.fixture(scope="function")
def driver():
    """
    Crea una instancia de Chrome en modo headless.
    Compatible con GitHub Actions y ejecución local.
    """
    chrome_options = Options()

    # Modo headless moderno
    chrome_options.add_argument("--headless=new")

    # Flags obligatorios para Linux (GitHub Actions)
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    # No pasamos el driver path → webdriver_manager lo gestiona automáticamente
    driver = webdriver.Chrome(options=chrome_options)

    yield driver
    driver.quit()



# =========================================================
# HOOK: CAPTURA DE PANTALLA ANTE FALLOS
# =========================================================
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:

        # Intentamos obtener 'driver' del test
        driver = (
            getattr(item.instance, 'driver', None)
            or getattr(item.cls, 'driver', None)
            or item.funcargs.get('driver', None)
        )

        # Buscar driver dentro de fixtures que devuelvan tuplas
        if not driver:
            fixture_names = ['login_fixture', 'cart_fixture']
            for f in fixture_names:
                val = item.funcargs.get(f, None)
                if isinstance(val, (tuple, list)) and len(val) > 0:
                    driver = val[0]
                    break

        # Si existe driver → guardar screenshot
        if driver:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            screenshot_dir = os.path.join(base_dir, "test", "screenshot")
            os.makedirs(screenshot_dir, exist_ok=True)

            screenshot_path = os.path.join(screenshot_dir, f"{item.name}.png")
            driver.save_screenshot(screenshot_path)

            print(f"\n[!] Screenshot guardado: {screenshot_path}")
