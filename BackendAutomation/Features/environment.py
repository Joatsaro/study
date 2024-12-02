import requests


def after_scenario(context, scenario):
    if "library" in scenario.tags:
        deleteBook_response = requests.post('http://216.10.245.166/Library/DeleteBook.php', json={
            'ID': context.bookID
            }, headers={'Content-Type': 'application/json}'},)
        assert deleteBook_response.status_code == 200
        res_json = deleteBook_response.json()
        print(res_json['msg'])
        assert res_json['msg'] == 'book is successfully deleted'