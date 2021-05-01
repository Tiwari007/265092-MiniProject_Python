# importing the module
import json


class UserDetails:
    def __init__(self, user_name, email, age, seat_choice):
        self.user_name = user_name
        self.email = email
        self.age = age
        self.seat_choice = seat_choice

    def save_data(self):
        user_dict = {
                     "name": self.user_name,
                     "email": self.email,
                     "age": self.age,
                     "seat_choice": self.seat_choice
                     }
        with open('User_Data.json', 'w') as user_save:
            json.dump(user_dict, user_save)

    def show_data(self):
        print("\nShowing data regarding user info.\n")
        with open('User_Data.json') as user_show:
            user_info = json.load(user_show)
        print("YOUR DETAILS ARE BELOW : - \n")
        print(user_info)


# login function - takes data as argument from json files regarding username and password.
# if details matches it shows "Sign In complete"
# Otherwise it shows different message according to wrong details
def login(data):
    if name in data:
        if password == data[name]:
            print("Sign In Complete...\nRedirecting to HomePage")
            homepage(name)
        else:
            print("password not match")
    else:
        print("User not found")


# signup function - takes data as a argument from json files regarding username and password.
# if details matches it shows "User already registered"
# Otherwise it saves all his details to an JSON file
# and create a new username and password an saves into json file
def signup(data):
    if name not in data:
        data[name] = password
        with open('data.json', 'w') as json_file_write:
            json.dump(data, json_file_write)
        print("USER REGISTER... \nNOW LOGIN AGAIN")
    else:
        print("user already registered")


# homepage function - takes user name as an argument
# this function is for booking his/her seats.
# as there are only 10 seats available.
# as the seats occupied it change the value from false to true in seats.json file
def homepage(name):
    with open('seats.json') as seats:
        seat_data = json.load(seats)

    print("\n\nWELCOME {} TO JET BOOKING SYSTEM\n".format(name))
    print("ENTER YOUR DETAILS FOR BOOKING... \n WE ONLY HAVE 10 SEATS ")
    user_name = input("ENTER YOUR NAME : - ")
    email = input("ENTER YOUR E-MAIL : - ")
    age = int(input("ENTER YOUR AGE : - "))

    print("CHOOSE YOUR SEATS FROM BELOW LIST\n")
    for s in seat_data:
        print(s, end=" ")
    seat_choice = input("\nENTER YOUR SEAT NUMBER : -")
    if not seat_data[seat_choice]:
        print("Seat reserved.\nYour seat number is {}".format(seat_choice))
        user = UserDetails(user_name, email, age, seat_choice)
        user.save_data()
        print("DO YOU WANNA SEE YOUR DETAILS : - \n1 - Show Details.\n2 - Exit()")
        if int(input()) == 1:
            user.show_data()
        else:
            exit(0)

        with open('seats.json', 'w') as seats_write:
            seat_data[seat_choice] = True
            json.dump(seat_data, seats_write)

        if input("Do you wanna book another seat...( yes / no )").lower() == "yes":
            homepage(name)
        else:
            exit()

    elif seat_data[seat_choice]:
        print("Seat Already Reserved...")
        if input("Do you wanna book another seat...( yes / no )").lower() == "yes":
            homepage(name)
        else:
            exit()
    else:
        print("Wrong Input")


with open('data.json') as json_file:
    data = json.load(json_file)

# MAIN CODE
# ask to user for enter login, signup or exit()
# according to user input() takes input for username and password
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
