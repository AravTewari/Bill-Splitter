class Movie:
    title = ""
    director = ""
    year = 0

    def __init__(self, title, director, year):
        self.year = year
        self.director = director
        self.title = title


# objects of the class Movie
titanic = Movie("Titanic", "James Cameron", 1997)
star_wars = Movie("Star Wars", "George Lucas", 1977)
fight_club = Movie("Fight Club", "David Fincher", 1999)
