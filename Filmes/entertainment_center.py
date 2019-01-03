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

breakingBed = media.Movie("Breaking Bed",
                          "Teste",
                          "https://http2.mlstatic.com/poster-cartaz-breaking-bad-a-40x60cm-D_NQ_NP_798928-MLB25905656574_082017-F.jpg",
                          "https://www.youtube.com/watch?v=ceqOTZnhgY8")

escola_de_Rock = media.Movie("Escola de Rock",
                          "Teste",
                          "http://br.web.img3.acsta.net/c_215_290/medias/nmedia/18/91/90/98/20169244.jpg",
                          "https://www.youtube.com/watch?v=-7zHtRk6pcI")

narcos = media.Movie("Narcos",
                          "Teste",
                          "https://img.elo7.com.br/product/zoom/1E0EB0A/poster-cartaz-narcos-netflix-poster-tematico.jpg",
                          "https://www.youtube.com/watch?v=U7elNhHwgBU")




movies = [toy_story, avatar, breakingBed, escola_de_Rock, narcos]
fresh_tomatoes.open_movies_page(movies)
