import requests
import json
url = "https://fakestoreapi.com/carts"
response = requests.get(url)

print(response)


json_data = '''
{
    "name":"KIM",
    "age":24,
    "hobbies":[
        "공부하기",
        "개빡공하기"
        ]
}
'''

data = json.loads(json_data)
print(data)
print(data['hobbies'][1])


