import requests

url = 'http://127.0.0.1:8000/api/'


headers = {
    'Authorization': 'Token 9732770221a634fc92d5cf842b03cac7fec69450'
}

r = requests.get(url,headers=headers)
print(r.text)