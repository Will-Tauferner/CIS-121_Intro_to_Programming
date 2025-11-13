class Tvshow:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre
    def get_genre(self):
        return self.genre
    def set_genre(self, genre):
        self.genre = genre
    def get_title(self):
        return self.title
    def set_title(self, title):
        self.title = title
    def preview(self):
        return f'the title is{self.title} and the genre is {self.genre}'
    

class NetflixDashboard:
    def __init__(self, profileShow):
        self.profileShow = profileShow
        self.shows = []
        
    def add_show(self, show):
        self.shows.append(show)


tvshow1 = Tvshow('friends','sitcom')
tvshow2 = Tvshow('Walking Dead', 'Horror')




