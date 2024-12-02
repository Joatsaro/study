import requests
from behave import *
from payLoad import *
from utilities.resources import *
from utilities.configurations import *


@given('the Book details which needs to be added to Library')
def step_impl(context):
    context.url = get_config()['API']['endpoint'] + ApiResources.addBook
    context.headers = {'Content-Type': 'application/json}'}
    context.payLoad = addBookPayload("tanipe", "433")

@when('we execute the AddBook PostAPI method')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payLoad, headers=context.headers,)

@then('book is successfully added')
def step_impl(context):
    #print(context.addBook_response.json())
    response_json = context.response.json()
    context.bookID = response_json['ID']
    #print(context.bookID)
    assert response_json['Msg'] == "successfully added"

@given('the Book details which {isbn} and {aisle}')
def step_impl(context, isbn, aisle):
    context.url = get_config()['API']['endpoint'] + ApiResources.addBook
    context.headers = {'Content-Type': 'application/json}'}
    context.payLoad = addBookPayload(isbn, aisle)

@given(u'I have github auth credentials')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = auth = ('Joatsaro', get_password())
    context.url = ApiResources.githubRepo

@when(u'I hit getRepo API of github')
def step_impl(context):
    context.response = context.se.get(context.url)


@then(u'status code of response should be {statuscode:d}')
def step_impl(context, statuscode):
    print(context.response.status_code)
    assert context.response.status_code == statuscode
