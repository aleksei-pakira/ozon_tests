import requests

url = "https://reqres.in/api/users"

payload = {"name": "morpheus", "job": "leader"}

response = requests.request("POST", url, data=payload)

print(response.text)


def test_api():
    response = requests.request("POST", url, data=payload)

    assert response.status_code == 201

def test_status_code():
    response1 = requests.request("POST", url)
    assert response1.status_code == 201, f"Expected status code 200, but got {response1.status_code}"


url2 = "https://ozon.ru/api/composer-api.bx/_action/addToCart"

response2 = requests.request("POST", url2)

print(response2.text)

def test_status_code2():
    response2 = requests.request("POST", url2)

    assert response2.status_code == 200