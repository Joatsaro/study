import requests
from payLoad import *
from utilities.resources import *
from utilities.configurations import *

url = get_config()['API']['endpoint'] + ApiResources.addBook
headers = {'Content-Type': 'application/json}'}
query = 'select * from Books'
addBook_response = requests.post(url, json=buildPayLoadFromDB(query), headers=headers,)
print(addBook_response.json())
response_json = addBook_response.json()
print(type(response_json))
bookID = response_json['ID']
print(bookID)
#
# # Delete Book
# deleteBook_response = requests.post('http://216.10.245.166/Library/DeleteBook.php', json={
#     'ID': bookID
#     }, headers={'Content-Type': 'application/json}'},)
# assert deleteBook_response.status_code == 200
# res_json = deleteBook_response.json()
# print(res_json['msg'])
# assert res_json['msg'] == 'book is successfully deleted'

# authentication
# se = requests.session()
# se.auth = auth = ('Joatsaro',get_password())
#
# url = 'https://api.github.com/user'
# github_response = se.get(url)
# print(github_response.status_code)
#
# url2 = 'https://api.github.com/user/repos'
# response = se.get(url2)
# print(response.status_code)

