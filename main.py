import re


# registration
def register():
    db = open("database.txt", "r")
    username = input("create username: ")
    regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

    def check(username):

        if re.search(regex, username):
            pass
        elif username == "@gmail.com" or "my@.in" or "123#@gmail.com":
            print("Invalid username,restart")
            register()
        else:
            print("Invalid username,restart")
            register()

    check(username)

    password = input("create password: ")
    flag = 0
    while True:
        if not re.search("[a-z]", password):
            flag = -1
            break
        elif not re.search("[A-Z]", password):
            flag = -1
            break
        elif not re.search("[0-9]", password):
            flag = -1
            break
        elif not re.search("[_@$]", password):
            flag = -1
            break
        elif re.search("\s", password):
            flag = -1
            break
        else:
            flag = 0
            pass
            break

    if flag == -1:
        print("Not a Valid Password")
        register()
    password1 = input("confirm password: ")

    d = []
    f = []
    for i in db:
        a, b = i.split(",")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))

    if password != password1:
        print("passwords dont match, restart")
        register()

    else:
        if len(password) not in range(5, 16):
            print("password should be in range(5,16), restart")
            register()
        elif username in d:
            print("username exists")
            register()
        else:
            db = open("database.txt", "a")
            db.write(username + "," + password + "\n")
            print("success")
            home()


# for Login
def access():
    db = open("database.txt", "r")
    username = input("username: ")
    password = input("password: ")

    if not len(username or password) < 1:
        d = []
        f = []
        for i in db:
            a, b = i.split(",")
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))
        try:
            if data[username]:
                try:
                    if password == data[username]:
                        print("login success")
                        print("Hi,", username)
                    else:
                        print("password incorrect")
                        option = input("Forgetpassword|Press any key to Retry:")      #FORGETPASSWORD
                        if option == "Forgetpassword":
                            print("your password is: " + data[username])
                            access()
                        else:
                            access()

                except:
                    print("incorrect password or username")
                    access()
            else:
                print("username or password are incorrect")
                access()
        except:
            print("your username not registered, Signup or Tryagain")               #USERNAME NOT FOUNT
            home()
    else:
        print("please enter a value")
        access()


# choosing option for Login or Signup
def home(option=None):
    option = input("Login | Signup: ")
    if option == "Login":
        access()
    elif option == "Signup":
        register()
    else:
        print("Please enter an option")
        home()


home()
