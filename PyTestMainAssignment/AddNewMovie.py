import csv


def addMovie():
    movieList = []
    title = input("Title : ")
    genre = input("Genre : ")
    length = input("Length : ")
    cast = input("Cast : ")
    director = input("Director : ")
    adminRating = input("Admin Rating : ")
    language = input("Language : ")
    timings = input("Timings : ")
    numOfShows = input("Number of shows in a day : ")
    firstShow = input("First Show : ")
    intervalTime = input("Interval Time :")
    gap = input("Gap Between Shows : ")
    capacity = input("Capacity : ")

    movieList = [title,
                 genre,
                 length,
                 cast,
                 director,
                 adminRating,
                 language,
                 timings,
                 numOfShows,
                 firstShow,
                 intervalTime,
                 gap,
                 capacity]

    with open("MovieDetails.csv", 'a', encoding='UTF8', newline='\n') as movieDetails:
        writer = csv.writer(movieDetails)
        writer.writerow(movieList)





