import webbrowser


# defining class movie
class Movie():
    """The class Movie stores movie name, storyline, poster image and youtube link

    Attributes:
        attr1 (str): movie title.
        attr2 (str): movie storyline.
        attr3 (str): movie poster image link.
        attr4 (str): movie trailer youtube link

    """
# defining init function and giving arguments to it
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# defining show trailer function
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
