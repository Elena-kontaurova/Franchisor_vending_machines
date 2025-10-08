import requests
import time

r = requests.get('http://127.0.0.1:8000/inform')
print(r.status_code, r.json(), '\n')

time.sleep(2)

tamd = {
    'podk': 'ol',
    'nastr': 'ol',
    'oblak': 'ol'
}

r = requests.post('http://127.0.0.1:8000/inform_post', params=tamd)
print(r.url)
print(r.status_code, r.json(), '\n')

time.sleep(2)

r = requests.put('http://127.0.0.1:8000/inform_put/6', params=tamd)
print(r.url)
print(r.status_code, r.json(), '\n')

time.sleep(2)

r = requests.delete('http://127.0.0.1:8000/inform_delete/1')
print(r.status_code, r.json(), '\n')
