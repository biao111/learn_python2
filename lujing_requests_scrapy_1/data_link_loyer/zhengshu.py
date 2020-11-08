import requests

response = requests.get('https://www.imooc.com',verify=False)
print(response.text)