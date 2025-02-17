from movie import Movie
import pickle
import os

movies = []


while True:
    option = int(input("To add a new movie press 1.\nTo see the list of movies you added press 2.\nTo exit the app press 3.\n"))

    if option == 1:
        
        if os.path.exists("watchlist.pkl"):
            with open("watchlist.pkl", "rb") as watchlist:
                movies = pickle.load(watchlist)
        
        in_title = input("Title: ")
        in_release_year = int(input("Release year: "))
        in_genre = input("Genre: ")
        in_imdb = input("IMDB url: ")
        
        movie = Movie(in_title, in_release_year, in_genre, in_imdb)
        movies.append(movie)
        
        with open("watchlist.pkl", "wb") as watchlist:
            pickle.dump(movies, watchlist)
            
    elif option == 2:
        with open("watchlist.pkl", "rb") as watchlist:
            movies = pickle.load(watchlist)
        
        for movie in movies:
            print(movie)
            
    elif option == 3:
       print("Goodbye!")
       break