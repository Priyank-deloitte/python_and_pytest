import csv

import Login


class RegisterUserData:
    pass


def register():
    print("****Create New Account****")
    name = input("Name : ")
    email = input("Email : ")
    phone = input("Phone No. : ")
    age = input("Age : ")
    password = input("Password : ")

    userDetails = [name, email, phone, age, password]

    with open('UserRegistration.csv', 'a', encoding='UTF8', newline='') as user:
        writer = csv.writer(user)
        writer.writerow(userDetails)

    print("Registration Successful")

    LoginObj = Login
    LoginObj.LoginPage()
