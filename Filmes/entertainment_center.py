# -*- coding: cp1252 -*-
import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "Historia de um menino e seu Brinquedo",
                        "https://upload.wikimedia.org/wikipedia/pt/thumb/d/dc/Movie_poster_toy_story.jpg/250px-Movie_poster_toy_story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                        "Avatar é um filme de ficcao cientifica",
                        "https://100grana.files.wordpress.com/2009/11/avatar_french.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")

movies = [toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)
