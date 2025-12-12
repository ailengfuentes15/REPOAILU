import requests

class PostPage:

    def __init__(self, base_url):
        self.base_url = base_url

    def post(self, endpoint="", json=None, headers=None):
        """
        Método genérico para POST.
        Devuelve la response completa.
        """
        url = f"{self.base_url}{endpoint}"

        try:
            response = requests.post(
                url,
                json=json,
                headers=headers
            )
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Error en POST: {e}")
            return None
