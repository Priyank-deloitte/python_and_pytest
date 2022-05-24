import pandas as pd


class Edit:
    pass


def editMovie():
    movieName = input("Enter movie name which has to be updated : ")

    while True:
        print("1. Title")
        print("2. Genre")
        print("3. Length")
        print("4. Cast")
        print("5. director")
        print("6. Admin Rating")
        print("7. Language")
        print("8. Timings")
        print("9. Number of Shows")
        print("10. First Show")
        print("11. Interval Time")
        print("12. Gap Between Shows")
        print("13. Capacity")
        print("14. Nothing to update")

        choice = int(input("Enter the updation choice : "))

        if choice == 1:
            newMovieName = input("Enter new movie name : ")
            df = pd.read_csv('MovieDetails.csv')
            df.loc[df['Title'] == movieName, 'Title'] = newMovieName
            df.to_csv('MovieDetails.csv', index=False)
            print(df)


        elif choice == 2:
            newGenre = input("Enter New Genre : ")
            df = pd.read_csv('MovieDetails.csv')
            df.loc[df['Title'] == movieName, 'Genre'] = newGenre
            df.to_csv('MovieDetails.csv', index=False)
            print(df)

        elif choice == 3:
            newLength = input("Enter New Length : ")
            df = pd.read_csv('MovieDetails.csv')
            df.loc[df['Title'] == movieName, 'Length'] = newLength
            df.to_csv('MovieDetails.csv', index=False)
            print(df)

        elif choice == 4:
            newCast = input("Enter New Cast : ")
            df = pd.read_csv('MovieDetails.csv')
            df.loc[df['Title'] == movieName, 'Cast'] = newCast
            df.to_csv('MovieDetails.csv', index=False)
            print(df)

        elif choice == 5:
            newDir = input("Enter New Director : ")
            df = pd.read_csv('MovieDetails.csv')
            df.loc[df['Title'] == movieName, 'Director'] = newDir
            df.to_csv('MovieDetails.csv', index=False)
            print(df)

        elif choice == 6:
            newAdminRating = input("Enter New Rating : ")
            df = pd.read_csv('MovieDetails.csv')
            df.loc[df['Title'] == movieName, 'Admin Rating'] = newAdminRating
            df.to_csv('MovieDetails.csv', index=False)
            print(df)

        elif choice == 7:
            newLanguage = input("Enter New Language : ")
            df = pd.read_csv('MovieDetails.csv')
            df.loc[df['Title'] == movieName, 'Language'] = newLanguage
            df.to_csv('MovieDetails.csv', index=False)
            print(df)

        elif choice == 8:
            newTiming = input("Enter New Timing : ")
            df = pd.read_csv('MovieDetails.csv')
            df.loc[df['Title'] == movieName, 'Timings'] = newTiming
            df.to_csv('MovieDetails.csv', index=False)
            print(df)

        elif choice == 9:
            newNum = input("Enter Number of Shows : ")
            df = pd.read_csv('MovieDetails.csv')
            df.loc[df['Title'] == movieName, 'Number of Shows'] = newNum
            df.to_csv('MovieDetails.csv', index=False)
            print(df)

        elif choice == 10:
            newFirstShow = input("Enter New time of the First Show : ")
            df = pd.read_csv('MovieDetails.csv')
            df.loc[df['Title'] == movieName, 'First Show'] = newFirstShow
            df.to_csv('MovieDetails.csv', index=False)
            print(df)

        elif choice == 11:
            newIntervalTime = input("Enter New Interval Time : ")
            df = pd.read_csv('MovieDetails.csv')
            df.loc[df['Title'] == movieName, 'Interval Time'] = newIntervalTime
            df.to_csv('MovieDetails.csv', index=False)
            print(df)

        elif choice == 12:
            newGap = input("Enter New Gap time : ")
            df = pd.read_csv('MovieDetails.csv')
            df.loc[df['Title'] == movieName, 'Gap Between Shows'] = newGap
            df.to_csv('MovieDetails.csv', index=False)
            print(df)

        elif choice == 13:
            newCapacity = input("Enter New Capacity : ")
            df = pd.read_csv('MovieDetails.csv')
            df.loc[df['Title'] == movieName, 'Capacity'] = newCapacity
            df.to_csv('MovieDetails.csv', index=False)
            print(df)

        elif choice == 14:
            break

        else:
            print("Enter a valid Choice!")
            break

        print("Updated Successfully!!")
