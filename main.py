import media
import fresh_tomatoes

data_toy = dict()
data_toy['movie_title'] = 'Toy Story'
data_toy['movie_storyline'] = 'A story of a boy and his toys that come to life'
data_toy['poster_image'] ='https://m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_SY1000_SX670_AL_.jpg'
data_toy['trailer_youtube']='https://www.youtube.com/watch?v=KYz2wyBy3kc'


data_avatar = dict()
data_avatar['movie_title'] = 'Avatar'
data_avatar['movie_storyline'] = 'A marine on an alien planet'
data_avatar['poster_image'] ='http://collider.com/wp-content/uploads/avatar_movie_poster_01.jpg'
data_avatar['trailer_youtube']='https://www.youtube.com/watch?v=5PSNL1qE6VY'

toy_story = media.Movie( data_toy['movie_title'] ,data_toy['movie_storyline'],
                    data_toy['poster_image'],data_toy['trailer_youtube'])

avatar_story = media.Movie( data_avatar['movie_title'] ,data_avatar['movie_storyline'],
                    data_avatar['poster_image'],data_avatar['trailer_youtube'])

movies = [toy_story,avatar_story]
# print(toy_story.storyline)
# print(avatar_story.storyline)
# avatar_story.show_trailer()
# fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.VALID_RATINGS)
# print(media.Movie.__doc__)
print(media.Movie.__module__)
