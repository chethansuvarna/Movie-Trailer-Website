'''I have referred udacity lessons to complete this project and i would like to give credits to udacity'''
import fresh_tomatoes
import media

# storing toy story in variable
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# storing avatar movie details in variable
avatar = media.Movie("Avatar",
                     "A story of marine soldiers in an alien planet",
                     "https://en.wikipedia.org/wiki/Avatar:_Music_from_the_Motion_Picture#/media/File:AvatarCover.JPG",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# storing bahubali_2 details in class Movie
bahubali_2 = media.Movie("Bahubali 2",
                         "A story of warriors",
                         "https://en.wikipedia.org/wiki/Baahubali_2:_The_Conclusion#/media/File:Baahubali_the_Conclusion.jpg",
                         "https://www.youtube.com/watch?v=G62HrubdD6o")

# storing movie details in a variable
_3_idiots = media.Movie("3 Idiots",
                        "A story of engineering students",
                        "https://en.wikipedia.org/wiki/3_Idiots#/media/File:3_idiots_poster.jpg",
                        "https://www.youtube.com/watch?v=xvszmNXdM4w")

# storing movie details in a variable
PK = media.Movie("PK",
                 "A story of an alien in INDIA ",
                 "http://im.rediff.com/movies/2014/aug/04aamir13.jpg",
                 "https://www.youtube.com/watch?v=SOXWc32k4zA")

# storing movie details in a variable
Finding_nemo = media.Movie("Finding Nemo",
                           "A story of a clown fish searching for his son",
                           "https://movieposters2.com/images/888913-b.jpg",
                           "https://www.youtube.com/watch?v=yDPRaVX2p8c")

# storing movie details in a variable
Parmanu = media.Movie("Parmanu",
                      "The story of how india become nuclear power nation",
                      "https://upload.wikimedia.org/wikipedia/en/d/da/Parmanu_film_poster.jpeg",
                      "https://www.youtube.com/watch?v=qN_9DnBh3hM")

# storing movie details in a variable
Gold = media.Movie("Gold",
                   "A story of India's first gold medal",
                   "https://upload.wikimedia.org/wikipedia/en/1/1f/Gold_2018_poster.jpg",
                   "https://www.youtube.com/watch?v=Pcv0aoOlsLM")

# storing movie details in a variable
Ant_man_and_wasp = media.Movie("Ant man and the Wasp",
                               "Story of  Ant man and Wasp",
                               "https://upload.wikimedia.org/wikipedia/en/2/2c/Ant-Man_and_the_Wasp_poster.jpg",
                               "https://www.youtube.com/watch?v=8_rTIAOohas")

# storing movies in a list
movie = [toy_story, avatar, bahubali_2, _3_idiots,
         PK, Finding_nemo, Parmanu, Gold, Ant_man_and_wasp]

# giving movie list to fresh_tomatoes and open_movies class to open the web page
#fresh_tomatoes.open_movies_page(movie)
#Parmanu.show_trailer()
