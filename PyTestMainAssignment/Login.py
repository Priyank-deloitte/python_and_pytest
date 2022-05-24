import csv

import AdminFunctionalities
import RegisterUserData
import UserLogin


class Error(Exception):
    pass


class InvalidCredentials(Error):
    pass


class UnregisteredUser(Error):
    pass


def LoginPage():
    while True:
        print("******Welcome to BookMyShow******")
        print("1. Login")
        print("2. Register new account")
        print("3. Exit")

        ch = int(input("Enter Action : "))

        AdminUserName = "Admin"
        AdminPassword = "Password@123"
        if ch == 1:
            print("******Welcome to BookMyShow******")
            print("1. Admin Login")
            print("2. User Login")
            choiceLogin = int(input("Enter the Login choice : "))

            if choiceLogin == 1:
                user = input("User : ")
                password = input("Password : ")
                try:
                    if user == AdminUserName and password == AdminPassword:
                        print("Admin Login Successfully")
                        adminObj = AdminFunctionalities
                        adminObj.adminWork()


                    else:
                        raise InvalidCredentials


                except InvalidCredentials:
                    print("Invalid Credentials Entered")

            elif choiceLogin == 2:
                DataFile = open("UserRegistration.csv", "r+")
                readFile = csv.reader(DataFile)
                value = len(list(readFile))
                email = input("Email : ")
                Password = input("Password : ")
                with open("UserRegistration.csv") as userDetails:
                    read = csv.DictReader(userDetails)
                    for i in read:
                        if i['Email'] != email or i['Password'] != Password:

                            continue

                        else:
                            print("User Login Successful")
                            name = i['Name']
                            userLoginObj = UserLogin
                            userLoginObj.user_Login(name)
                            break

                try:
                    if value == 1:
                        raise UnregisteredUser


                except UnregisteredUser:
                    print("Unregistered User, Registration Required!!")



        elif ch == 2:
            registerUserObj = RegisterUserData
            registerUserObj.register()


        elif ch == 3:
            exit(0)

        else:
            print("Enter Valid Choice")


class Login:
    pass
