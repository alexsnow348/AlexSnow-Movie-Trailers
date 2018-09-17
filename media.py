import webbrowser as wb


class Movie(object):
    """Movie Class docstring
    This class provides a way to store movie related informationself.

    Attributes:
        title(str): The title of the movie.
        storyline(str): The short summary of the movie.
        poster_image (str): The URL for the movie poster.
        trailer(str): The Youtube URL for the trailer of the movie.

    """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, storyline, poster_image, trailer):
        super(Movie, self).__init__()
        self.title = title
        self.storyline = storyline
        self.poster_image = poster_image
        self.trailer = trailer

    @property
    def show_trailer(self):
        wb.open(self.trailer_youtube_url)
