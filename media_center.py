import trailer
import fresh_tomatoes

midnight_in_paris = trailer.Movie('Midnight in Paris',
                                  'A man gets transported to golden era Paris from modern days',
                                  'https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg',
                                  'https://www.youtube.com/watch?v=FAfR8omt-CY')

pursuit_of_happiness = trailer.Movie('The Pursuit of Happiness',
                                     'A guy\'s fight to save his career and his family',
                                     'https://en.wikipedia.org/wiki/The_Pursuit_of_Happyness#/media/File:Poster-pursuithappyness.jpg',
                                     'https://www.youtube.com/watch?v=89Kq8SDyvfg')

dark_knight = trailer.Movie('The Dark Knight',
                            'Batman\'s continued struggle to clean up the city of Gotham',
                            'https://en.wikipedia.org/wiki/The_Dark_Knight_(film)#/media/File:Dark_Knight.jpg',
                            'https://www.youtube.com/watch?v=EXeTwQWrcwY')

schindlers_list = trailer.Movie('Schindler\'s List',
                                'One man\'s fight to save jews from the Nazi gas chambers',
                                'https://en.wikipedia.org/wiki/Schindler%27s_List#/media/File:Schindler%27s_List_movie.jpg',
                                'https://www.youtube.com/watch?v=gG22XNhtnoY')

inception = trailer.Movie('Inception',
                          'Inside one\'s dream',
                          'https://en.wikipedia.org/wiki/Inception#/media/File:Inception_(2010)_theatrical_poster.jpg',
                          'https://www.youtube.com/watch?v=YoHD9XEInc0')

interstellar = trailer.Movie('Interstellar',
                             'A quest to search for a habitable planet like earth',
                             'https://en.wikipedia.org/wiki/Interstellar_(film)#/media/File:Interstellar_film_poster.jpg',
                             'https://www.youtube.com/watch?v=zSWdZVtXT7E')
movies = [midnight_in_paris, pursuit_of_happiness, dark_knight, schindlers_list, inception, interstellar]
fresh_tomatoes.open_movies_page(movies)
