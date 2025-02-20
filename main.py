import pandas as pd

while True:
    option = int(input("To add a new movie press 1.\nTo see the list of movies you added press 2.\nTo exit the app press 3.\n"))

    if option == 1:
        in_title = input("Title: ")
        in_release_year = int(input("Release year: "))
        in_genre = input("Genre: ")
        in_imdb = input("IMDB url: ")
        
        df = pd.DataFrame(data=[[in_title, in_release_year, in_genre, in_imdb]], columns=["title", "release", "genre", "imdb"])
        df.to_csv("watchlist.csv", index=False)
            
    elif option == 2:
        df = pd.read_csv("watchlist.csv")
        print(df.to_string())
           
    elif option == 3:
       print("Goodbye!")
       break