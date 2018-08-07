import trailer
import fresh_tomatoes

midnight_in_paris = trailer.Movie('Midnight in Paris',
                                  'A man gets transported to golden era\
                                   Paris from modern days',
                                  'https://upload.wikimedia.org/wikipedi' +
                                  'a/en/9/9f/Midnight_in_Paris_Poster.jpg',
                                  'https://www.youtube.com/wat' +
                                  'ch?v=FAfR8omt-CY')

pursuit_of_happiness = trailer.Movie('The Pursuit of Happiness',
                                     'A guy\'s fight to save his career\
                                      and his family',
                                     'https://upload.wikimedia.org/wikipedi' +
                                     'a/en/8/81/Poster-pursuithappyness.jpg',
                                     'https://www.youtube.com/watc' +
                                     'h?v=89Kq8SDyvfg')

dark_knight = trailer.Movie('The Dark Knight',
                            'Batman\'s continued struggle to clean\
                            up the city of Gotham',
                            'https://upload.wikimedia.org/wikipedi' +
                            'a/en/8/8a/Dark_Knight.jpg',
                            'https://www.youtube.com/watch?v=E' +
                            'XeTwQWrcwY')

schindlers_list = trailer.Movie('Schindler\'s List',
                                'One man\'s fight to save jews from the\
                                 Nazi gas chambers',
                                'https://upload.wikimedia.org/wikipedi' +
                                'a/en/3/38/Schindler%27s_List_movie.jpg',
                                'https://www.youtube.com/watch?v=gG22XNhtnoY')

inception = trailer.Movie('Inception',
                          'Inside one\'s dream',
                          'https://upload.wikimedia.org/wikipedia/en/2/2e/I' +
                          'nception_%282010%29_theatrical_poster.jpg',
                          'https://www.youtube.com/watch?v=YoHD9XEInc0')

interstellar = trailer.Movie('Interstellar',
                             'A quest to search for a habitable planet \
                             like earth',
                             'https://upload.wikimedia.org/wikipedia/en/b/b' +
                             'c/Interstellar_film_poster.jpg',
                             'https://www.youtube.com/watch?v=zSWdZVtXT7E')
movies = [midnight_in_paris, pursuit_of_happiness, dark_knight,
          schindlers_list, inception, interstellar]

fresh_tomatoes.open_movies_page(movies)
