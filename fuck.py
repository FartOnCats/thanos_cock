

import requests

def forumData():
    data = {
        name: "bruh",
        price: 69,
        image: "https://i.ytimg.com/vi/wUAftsmzl9M/maxresdefault.jpg",
        description: "lol",
    }
    return data

r = requests.get('https://salty-reef-80979.herokuapp.com/campgrounds')
print(r.status_code)