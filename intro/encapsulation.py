class Movie:
    def __init__(self, movie=None):
        self.__movie = None # encapsuled
        
    def set_movie(self, movie):
        self.__movie = movie
        
    def get_movie(self):
        return self.__movie

if __name__ == "__main__":
    m = Movie()
    m.set_movie("RRR")
    print(m.get_movie())

# advantages:
# - Simpler to maintain
# - Increases flexibility by choosing read only write only variables
# - Which data member we wish to keeep hidden or accessible can be specified