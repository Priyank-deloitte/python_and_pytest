import csv

import AddNewMovie
import DeleteMovie
import EditMovie
import Login


class Error(Exception):
    pass


class No_Movies(Error):
    pass


class AdminFunctionalities:
    pass


def adminWork():
    while True:
        print("*****Welcome Admin*****")
        print("1. Add new movie info")
        print("2. Edit movie info")
        print("3. Delete movies")
        print("4. Logout")

        choice = int(input("Enter choice : "))

        if choice == 1:

            addNewObj = AddNewMovie
            addNewObj.addMovie()

        elif choice == 2:
            try:
                DataFile = open("MovieDetails.csv", "r+")
                readFile = csv.reader(DataFile)
                value = len(list(readFile))
                if value > 1:
                    editMovieObj = EditMovie
                    editMovieObj.editMovie()

                else:
                    raise No_Movies

            except No_Movies:
                print("No movie inside the movie file to edit.")

        elif choice == 3:
            try:
                DataFile = open("MovieDetails.csv", "r+")
                readFile = csv.reader(DataFile)
                value = len(list(readFile))
                if value > 1:
                    deleteMovieObj = DeleteMovie
                    deleteMovieObj.delete()
                else:
                    raise No_Movies

            except No_Movies:
                print("No movie inside the movie file to delete")

        elif choice == 4:
            print("Logged Out Successfully")
            returnLoginObj = Login
            returnLoginObj.LoginPage()
            break

        else:
            print("Enter Valid Option")
            break
