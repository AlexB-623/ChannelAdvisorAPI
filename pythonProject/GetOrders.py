import requests
import json
import AccessCode

token = AccessCode.func_get_code()
url = "https://api.channeladvisor.com/v1/Orders?&$skip=0"
headers = {
  'Authorization': '',
  'Content-Type': 'application/json'
}
headers['Authorization'] = str("Bearer " + token)
print(headers)
response = requests.request("GET", url, headers=headers)

print(response.text)
