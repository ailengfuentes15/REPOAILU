import requests
import pytest

#@pytest.mark.skip(reason="Desactivada porque sigue en desarrollo")
def test_get_users(url_base,header_request):
    url = f"{url_base}/2"

    response = requests.get(url,headers=header_request)

    # VERIFICAR QUE LA RESPUESTA SEA EXITOSA
    assert response.status_code == 200

    data = response.json()

    # VERIFICAR QUE LA CLAVE "DATA" ESTA PRESENTE
    assert "data" in data

    # VERIFICAR QUE HAYA AL MENOS UN USUARIO EN LA LISTA
    assert len(data["data"]) > 0
