class Movie(object):

    def __init__(self, source, name, year, rating, description):
        self.source = source
        self.name = name
        self.year = year
        self.rating = rating
        self.description = description

    def addMovie(self, name):
        test = name

    def deleteMovie(self, name):
        test = name

dracula = Movie('nflix', 'Dracula', 2000, 4.5, 'bla, bla, bla')

print(dracula.year)



