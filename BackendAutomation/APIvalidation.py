import requests
import json

response = requests.get('http://216.10.245.166/Library/GetBook.php',
                        params={'AuthorName': 'Rahul Shetty2'},)
# print(response.text)
# type(response.text)
# dict_response = json.loads(response.text)
# print(type(dict_response))
# print(dict_response[0]['isbn'])
json_response = response.json()
print(type(json_response))
print(json_response)
print(json_response[0]['isbn'])
assert response.status_code == 200
print(response.headers)
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'
# Retrieve the book details with isbn bcz888effed
for actualBook in json_response:
    if actualBook['isbn'] == 'bcz888effed':
        actualRealBook = actualBook

expectedBook = {
    "book_name": "Learn Appium Automation with Java",
    "isbn": "bcz888effed",
    "aisle": "200278"
    }


print(type(expectedBook))
assert actualRealBook == expectedBook


