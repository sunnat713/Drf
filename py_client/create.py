import requests

headers = {'Authorization': 'Token 47bc0ed1f77ef335d11c1342d72d703d1b7528bf'}

endpoint = 'http://localhost:8000/api/product/'

get_response = requests.get(endpoint, headers=headers)
print(get_response.json())
