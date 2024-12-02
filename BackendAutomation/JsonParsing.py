import json

# courses = '{"name": "AtanacioSaquelares","languages": ["Java","Python"]}'

# Loads method parse json string and it return dictionary
# dict_courses = json.loads(courses)
# print(type(dict_courses))
# print(dict_courses)
# print(dict_courses['name'])

# Get me the first language taught by trainer
# list_languages = dict_courses['languages']
# print(type(list_languages))
# print(list_languages[0])
# print(dict_courses['languages'][0])

# ******* Parse content present in Json file
with open('/Users/asaquelares/Documents/python-training/pytestDemo/BackendAutomation/course.json') as f:
    data = json.load(f)
    # print(data)
    # print(type(data))
    # print(data['courses'])
    # print(data['courses'][0])
    # print(data['courses'][1])
    # print(data['courses'][1]['title'])
    # print(data['dashboard']['website'])

# price of course 'RPA'
    print(type(data['courses']))
    for course in data['courses']:
        # print(course)
        if course['title'] == 'RPA':
            print(course['price'])
            assert course['price'] == 45

with open('/Users/asaquelares/Documents/python-training/pytestDemo/BackendAutomation/course1.json') as fi:
    data2 = json.load(fi)
    assert data == data2

