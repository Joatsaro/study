from utilities.configurations import *


def addBookPayload(isbn, aisle):
    body = {
        'name': 'Learn Appium Automation with Java',
        'isbn': isbn,
        'aisle': aisle,
        'author': 'John Foe'
    }
    return body


def buildPayLoadFromDB(query):
    addBody = {}
    tp = get_query(query)
    addBody['name'] = tp[0]
    addBody['isbn'] = tp[1]
    addBody['aisle'] = tp[2]
    addBody['author'] = tp[3]
    return addBody
