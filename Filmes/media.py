import webbrowser

class Movie():
    def __init__ (testeSelf,movie_title, movie_storyline, poster_image,
                  trailer_youtube):
        testeSelf.title = movie_title
        testeSelf.storyline = movie_storyline
        testeSelf.poster_image_url = poster_image
        testeSelf.trailer_youtube_url = trailer_youtube 

    def show_trailer(testeSelf):
        webbrowser.open(testeSelf.trailer_youtube_url)
