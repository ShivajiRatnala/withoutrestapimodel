import json

import requests
# A=' http://127.0.0.1:8000/'
# B='api1/'
# def get_response():
#     resp=requests.get(A+B)
#     print(resp.status_code)
#     print(resp.json())
# get_response()

# A=' http://127.0.0.1:8000/'
# B='api2/'
# def get_response(id):
#     resp=requests.get(A+B+id)
#     print(resp.status_code)
#     print(resp.json())
# id=input('enter id: ')
# get_response(id)


# A=' http://127.0.0.1:8000/'
# B='api4/'
# def get_all():
#     resp=requests.get(A+B)
#     print(resp.status_code)
#     print(resp.json())
# get_all()


# A=' http://127.0.0.1:8000/'
# B='api5/'
# def get_all():
#     resp=requests.get(A+B)
#     print(resp.status_code)
#     print(resp.json())
# get_all()

A=' http://127.0.0.1:8000/'
B='api6/'
def post_data():
    New_data={
        'name':'rasi',
        'cls':'12th',
        'school': 'govt',
        'Address':'india',
    }
    resp=requests.post(A+B,data=json.dumps(New_data))
    print(resp.status_code)
    print(resp.json())
post_data()