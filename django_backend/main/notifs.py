import requests
def notify_users(user,message):
    PARAMS = {'user':user,'message':message}
    r = requests.post(url = 'http://localhost:8000/push/', params = PARAMS)