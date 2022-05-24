import csv

import pandas as pd


class BookingTickets:
    pass


def book(Movie, Name):
    with open("MovieDetails.csv") as movieDetail:
        read = csv.DictReader(movieDetail)

        for row in read:
            if row['Title'] == Movie:
                timing = row['Timings']
                break

        timingList = timing.split(",")
        for time in range(len(timingList)):
            print("Press ", time + 1, " for selecting time slot of", timingList[time])

        selectTime = int(input("Enter value for choosing the time : "))

        for time in range(len(timingList)):
            if time + 1 == selectTime:
                print("Timing : ", timingList[time])

        remainingSeat = int(row['Capacity'])
        print("Remaining Seat : ", remainingSeat)

        numOfSeats = int(input("Enter the number of seats you want to book : "))

        if remainingSeat >= numOfSeats:
            seatLeft = remainingSeat - numOfSeats
            seatRemain = str(seatLeft)
            df = pd.read_csv('MovieDetails.csv')
            df.loc[df['Title'] == Movie, 'Capacity'] = seatLeft
            df.to_csv('MovieDetails.csv', index=False)
            print(df)

            print("Booking Successfull ! Thanks for Booking through BookMyShow")

        else:
            print("Seats Unavailable!!!")
