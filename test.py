import requests
from  urllib.parse import urljoin

BASE = 'http://localhost:5000/'
def testing_user_update(user_input):
    API = 'user'
    URL = urljoin(BASE, API)
    r = requests.post(URL, json=user_input)
    print(r.json(), r.status_code)

def testing_descending_id():
    API = 'user/descending_id'
    URL = urljoin(BASE, API)
    r = requests.get(URL)
    print(r.text, r.status_code)

if __name__ == '__main__':
#    user_input = {
#            'name': 'quan',
#            'email': 'trewq@poiu.com',
#            'address': '312 boulevard somewhere',
#            'phone': '29488'
#        }
#    testing_user_update(user_input)

    testing_descending_id()
