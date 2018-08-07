import webbrowser


class Movie:
    """
    Represents a movie consisting of title, storyline, poster, and trailer url.

    Attributes:
        title (str) : movie name
        storyline (str) : Sort movie synopsys
        poster_image_url (str) : movie poster image url
        movie_trailer (str) : youtube url for movie trailer
    """

    def __init__(self,
                 movie_title,
                 movie_storyline,
                 movie_poster,
                 movie_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer

    def show_trailer(self):
        """Call this method to play movie trailer"""
        webbrowser.open(self.trailer_youtube_url)
