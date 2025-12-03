import pytest
import os
from datetime import datetime

@pytest.fixture
def url_base():
    return "https://reqres.in/api/users"

@pytest.fixture
def header_request():
    return {"x-api-key": "reqres-free-v1"}



@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):

    """
        Hook de Pytest que se ejecuta después de cada prueba para generar un reporte.
        Si la prueba falla y existe un objeto driver toma una captura de pantalla y la guarda en el directorio test/screenshot
        con el nombre de la prueba.
    """
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = getattr(item.instance, 'driver', None) \
              or getattr(item.cls, 'driver', None) \
              or item.funcargs.get('driver', None)
        
        # Si no se encuentra 'driver' directamente, buscar en fixtures comunes que retornan tuplas
        if not driver:
            # Lista de fixtures comunes que retornan tuplas con driver como primer elemento
            fixture_names = ['login_fixture', 'cart_fixture']
            for fixture_name in fixture_names:
                fixture_value = item.funcargs.get(fixture_name, None)
                if fixture_value:
                    # Si el fixture retorna una tupla/lista, el driver es el primer elemento
                    if isinstance(fixture_value, (tuple, list)) and len(fixture_value) > 0:
                        driver = fixture_value[0]
                        break
        
        if driver:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            screenshot_dir = os.path.join(base_dir, "test", "screenshot")
            os.makedirs(screenshot_dir, exist_ok=True)

            screenshot_path = os.path.join(screenshot_dir, f"{item.name}.png")
            driver.save_screenshot(screenshot_path)
            print(f"\n[!] Screenshot guardado: {screenshot_path}")

