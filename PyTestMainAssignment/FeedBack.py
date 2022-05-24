import csv


class FeedBack:
    pass


def rating(Movie, Name):
    userRating = input("Enter Rating for this movie : ")
    feedBackList = [Name, Movie, userRating]

    with open("Feed_Back.csv", 'a', encoding='UTF8', newline='\n') as userReview:
        writer = csv.writer(userReview)
        writer.writerow(feedBackList)

    print("Thankyou for your Feedback!!")
