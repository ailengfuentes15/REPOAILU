import requests


class GetPage:

    def __init__(self, base_url):
        """
        Recibe la base_url desde el conftest.py
        para que la configuración quede centralizada.
        """
        self.base_url = base_url

    def get(self, endpoint="", params=None, headers=None):
        """
        Método genérico para solicitudes GET.

        :param endpoint: string (ej: "/posts/1")
        :param params: dict con query params
        :param headers: dict con headers opcionales
        :return: objeto Response de requests
        """
        url = f"{self.base_url}{endpoint}"

        try:
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Error al realizar GET: {e}")
            return None
