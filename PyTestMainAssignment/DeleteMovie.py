import csv

import pandas as pd


class Error(Exception):
    pass


class NoMoviePresent(Error):
    pass


class DeleteMovie:
    pass


def delete():
    delMovie = input("Enter the movie to delete : ")

    try:
        invalidMovie = False
        with open('MovieDetails.csv') as movieDetails:
            read = csv.DictReader(movieDetails)
            for row in read:
                if row['Title'] != delMovie:
                    invalidMovie = True
                    continue

                else:
                    df = pd.read_csv('MovieDetails.csv')
                    df.drop(df[df['Title'] == delMovie].index, inplace=True)
                    df = df.to_csv('MovieDetails.csv', index=False)
                    print("Movie is Deleted Successfully!!")
                    break

            if not invalidMovie:
                raise NoMoviePresent

    except NoMoviePresent:
        print("No Such Movie present in the Database with name : ", delMovie)
