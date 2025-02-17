class Movie:
    def __init__(self, title, release_year, genre, imdb_url):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.imdb_url = imdb_url
        
        
    def __str__(self):
        return f'\n***************MOVIE***************\nTitle: {self.title}\nRelease year: {self.release_year}\nGenre: {self.genre}\nIMDB link: {self.imdb_url}\n'
