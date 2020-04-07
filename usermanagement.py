import random
import string
intro = """Enter firstname, lastname and email separated by coma(,)
        E.G >> Moses, Oghene, mosesoghene@gmail.com"""
users = []
def get(a, b):
    finit = a[:2]
    linit = b[-2:]
    letters = string.ascii_letters
    rand = ''.join(random.choice(letters) for i in range(5))
    return  finit + linit + rand

while True:
    print(intro)
    data = input(">> ")
    fname, lname, email = data.split(", ")
    pwd = get(fname, lname)
    prompt = input(f"Are you satisfied with password: {pwd}. Y/N >> ").lower()
    if prompt == 'y':
        dict = {"Username: " + fname: {'firstname': fname, 'lastname': lname,  'email': email, 'password': pwd}}
        users.append(dict)
        print(users[-1])
        rerun = input("Do you want to enter another user? Y/N >> ").lower()
        if rerun == "y":
            continue
        else:        
            print("All Users: \n")      
            for i in users:
                print(i)
            break
    else:
        while True:
            pwd = input("Enter your preferred password >> ")
            if len(pwd) < 7:
                print("password must be greater than 7 characters")
                continue
            else:
                dict = {"Username: " + fname: {'firstname': fname, 'lastname': lname, 'email': email, 'password': pwd}}
                users.append(dict)
                print(users[-1])
                rerun = input("Do you want to enter another user? Y/N >> ").lower()
                if rerun == "y":
                    continue
                else:   
                    print("All Users: \n")         
                    for i in users:
                        print(i)
                    break
        break
        


