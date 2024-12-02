import requests
from behave import *
from pytestDemo.BackendAutomation.payLoad import *
from pytestDemo.BackendAutomation.utilities.resources import *
from pytestDemo.BackendAutomation.utilities.configurations import *


@given('the Book details which needs to be added to Library')
def step_impl(context):
    context.url = get_config()['API']['endpoint'] + ApiResources.addBook
    context.headers = {'Content-Type': 'application/json}'}
    context.payLoad = addBookPayload("manfddt")

@when('we execute the AddBook PostAPI method')
def step_impl(context):
    context.addBook_response = requests.post(context.url, json=buildPayLoadFromDB(query), headers=context.headers,)

@then('book is successfully added')
def step_impl(context):
    print(context.addBook_response.json())
    response_json = context.addBook_response.json()
    bookID = response_json['ID']
    print(bookID)
    assert response_json['Msg'] == "successfully added"


