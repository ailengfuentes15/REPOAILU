import requests

encabezado = {"x-api-key": "reqres-free-v1"}
url = "https://reqres.in/api/users/2"

response = requests.get(url,headers=encabezado)

print(response.status_code)
data = response.json()
print(data)