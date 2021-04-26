# importing the module
import json

def do_you_want_to_contimue():
    pass


def login(data):
    if name in data:
        if password == data[name]:
            print("Sign In Complete...\nRedirecting to HomePage")
            homepage(name)
        else:
            print("password not match")
    else:
        print("User not found")


def signup(data):
    if name not in data:
        data[name] = password
        with open('data.json', 'w') as json_file_write:
            json.dump(data, json_file_write)
        print("USER REGISTER... \nNOW LOGIN AGAIN")
    else:
        print("user already registered")


def homepage(name):
    seats = {
        "1A": False,
        "2A": False,
        "3A": False,
        "4A": False,
        "5A": False,
        "6A": False,
        "7A": False,
        "8A": False,
        "9A": False,
        "10A": False

    }
    print("\n\nWELCOME {} TO JET BOOKING SYSTEM\n".format(name))
    print("ENTER YOUR DETAILS FOR BOOKING... \n WE ONLY HAVE 10 SEATS ")
    print("CHOOSE YOUR SEATS FROM BELOW LIST")
    for s in seats:
        print(s, end=" ")
    seat_choice = input("\nENTER YOUR SEAT NUMBER : -")
    if seat_choice:
        print("Seat reserved.\nYour seat number is {}".format(seat_choice))
        seats[seat_choice] = True
        print(seats)
        if input("Do you wanna book another seat...( yes / no )").lower() == "yes":
            do_you_want_to_contimue()
        else:
            exit()
    elif not seat_choice:
        print("Seat Already Reserved...")
        if input("Do you wanna book another seat...( yes / no )").lower() == "yes":
            do_you_want_to_contimue()
        else:
            exit()
    else:
        print("Wrong Input")

with open('data.json') as json_file:
    data = json.load(json_file)

# MAIN CODE
print("Welcome to jet booking.\nBefore further proceeding choose one of these : -")
print("""
1 - SIGN IN (FOR REGISTERED USER)
2 - SIGN UP (FOR NEW USER)
3 - EXIT
""")
choice = int(input())
if choice == 1:
    print("Welcome to Sign In Process...")
    # User input() for signing
    print("_____Fill all credentials_____")
    name = input("Enter Your name : - ")
    password = input("Enter Your password : -")
    login(data)


elif choice == 2:
    print("Welcome New User to Signup Process...")
    # User input() for signing
    print("_____Fill all credentials_____")
    name = input("Enter Your name : - ")
    password = input("Enter Your password : -")
    signup(data)


elif choice == 3:
    exit()
