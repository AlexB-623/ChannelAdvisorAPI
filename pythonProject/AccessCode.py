import requests
import getpass
import urllib.parse


def func_get_code():
    client_id = input("Enter client_ID: ")
    authorization_basic = input("Enter Authorization after Basic: ")
    grant_type = "soap"
    scope = "orders%20inventory"
    developer_key = "783b8fd0-6a2e-40e0-9797-991bb96d8986"
    ### How does this work?
    password = getpass.getpass(prompt='Password: ', stream=None)
    account_id = "d4b4efae-c7ef-4f7d-9969-abb9d5b55f0a"
    url = "https://api.channeladvisor.com/oauth2/token"
    payload = "client_id=" + client_id + "&grant_type=" + grant_type + "&scope=" + scope + "&developer_key=" + developer_key + "&password=" + password + "&account_id=" + account_id
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': str('Basic ' + authorization_basic)
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    full_response = eval(response.text)
    full_response["ResponseStatusCode"] = response
    token = full_response["access_token"]
    return token


code = func_get_code()
print(code)
#print(type(code))