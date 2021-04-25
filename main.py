import Authentication
import login_successfull

dictionary = {"Bucky": "11111", "Alita": "22222"}


print("IF YOU ARE NEW ON THIS PLEASE REGISTER.\nOR IF YOU'RE ALREADY A MEMBER JUST LOGIN\n")
print("1 -> LOGIN\n2 -> SIGNUP\n3 -> EXIT")

choice = int(input())
if choice == 1:
    name = input()
    password = input()
    if Authentication.login(name, password, dictionary):
        print("Welcome {}".format(name))
        login_successfull.play_area()
    else:
        print("This is not a right credential. \nExiting program ")
        exit(0)
elif choice == 2:
    name = input()
    password = input()
    if Authentication.signup(name, password, dictionary):
        login_successfull.play_area()
    else:
        print("Exiting Program")
        exit(0)
elif choice == 3:
    exit(0)






