import random
import string
intro = """Enter firstname, lastname and email separated by coma(,)
        E.G >> Moses, Oghene, mosesoghene@gmail.com"""
users = {}
def get(a, b):
    finit = a[:2]
    linit = b[-2:]
    letters = string.ascii_letters
    rand = ''.join(random.choice(letters) for i in range(5))
    return  finit + linit + rand

while True:
    print(intro)
    data = input("CRTL + C to close >> ")
    fname, lname, email = data.split(", ")
    pwd = get(fname, lname)
    prompt = input(f"Are you satisfied with password: {pwd}. Y/N").lower()
    if prompt == 'y':
        dict = {fname: {'firstname': fname, 'lastname': lname,  'email': email, 'password': pwd}}
        users.update(dict)
        print(users[fname])
        print(users)
    else:
        while True:
            pwd = input("Enter your preferred password >> ")
            if len(pwd) < 7:
                print("password must be greater than 7 characters")
                continue
            else:
                dict = {fname: {'firstname': fname, 'lastname': lname, 'email': email, 'password': pwd}}
                users.update(dict)
                print(users[fname])
                print(users)
                break
        


