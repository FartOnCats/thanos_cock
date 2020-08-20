

import requests

def forumData():
    data = {
        'name': "bruh",
        'price': 69,
        'image': "https://i.ytimg.com/vi/wUAftsmzl9M/maxresdefault.jpg",
        'description': "lol",
    }
    return data

r = requests.Session()

#login
r.post('https://salty-reef-80979.herokuapp.com/login',data={'username':'admin','password':'admin'})

#send meme
for i in range(5000):
    x = r.post('https://salty-reef-80979.herokuapp.com/campgrounds',data=forumData())
    print(x.status_code)