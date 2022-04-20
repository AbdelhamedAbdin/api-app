import requests as request


# endpoint = "http://localhost:8000/api/"
# endpoint = "http://localhost:8000/api/1"
endpoint = "http://localhost:8000/api/auth/"
password = input("type password: ")
auth_response = request.post(endpoint, json={'username': 'medoabdin', 'password': password})

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    endpoint = "http://localhost:8000/api/"
    headers = {
        "Authorization": f"Token {token}"
    }

    get_response = request.get(endpoint, headers=headers)
    print(get_response.json())
    print(token)


# get_response = request.post(endpoint, json={'content': 'Hello'})
# get_response = request.post(endpoint, json={'title': 'create by function based view'})
