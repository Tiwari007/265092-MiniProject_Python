def login(name, password, dictionary):
    if name in dictionary:
        if password == dictionary[name]:
            print("Login Successful")
            return True
        else:
            print("Login Unsuccessful")
            return False


def signup(name, password, dictionary):
    if name not in dictionary:
        dictionary[name] = password
        print(dictionary)
        print("USER REGISTERED ... REDIRECTING TO HOMEPAGE")
        return True
    else:
        print("User Already Registered")
        return False
