import requests

url = "https://reqres.in/api/users"

payload = {"name": "morpheus", "job": "leader"}

response = requests.request("POST", url, data=payload)

print(response.text)


def test_api():
    response = requests.request("POST", url, data=payload)

    assert response.status_code == 201


