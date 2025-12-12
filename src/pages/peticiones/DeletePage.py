import requests

class DeletePage:

    def __init__(self, base_url):
        self.base_url = base_url

    def delete(self, endpoint="", headers=None):
        """
        Método genérico DELETE.
        Devuelve response o None si falla.
        """
        url = f"{self.base_url}{endpoint}"

        try:
            response = requests.delete(url, headers=headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Error en DELETE: {e}")
            return None
