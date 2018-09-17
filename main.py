import media
import fresh_tomatoes
import requests as rq
import json

# Global variables
BASE_URL = 'https://api.themoviedb.org/3/'
MOVIE_PATH = 'movie/top_rated'
APIKEY = '33c5e456ec2cf3f3a7b1bacc1996984d'
LANGUAGE = 'en-US'
PAGE = 1
IMG_PATH = 'https://image.tmdb.org/t/p/w1280'
TOTAL_MOVIE_TO_DISPLAY = 6


def get_trailer(id):
    """ This function return the youtube video url.
    Args:
        id (int): id for the selected movie.

    Returns:
        video_source(str): The return video source url.
    """
    url = BASE_URL + 'movie/%s/videos?api_key=%s&language=%s&page=%s' % \
        (id, APIKEY, LANGUAGE, PAGE)
    content = rq.get(url)
    data = content.text
    data = json.loads(data)
    data = data['results']
    video_source = str()
    for each in data:
        if each['type'] == 'Trailer':
            video_source = 'https://www.youtube.com/watch?v=' + each['key']
            break
    return video_source


def get_details():
    """ This function produces movie details data.

    Returns:
        output_list(list): the details movie list return.
    """
    output_list = list()
    url = BASE_URL + '%s?api_key=%s&language=%s&page=%s' % (MOVIE_PATH, APIKEY,
                                                            LANGUAGE, PAGE)
    content = rq.get(url)
    data = content.text
    data = json.loads(data)
    data = data['results']
    data = data[:TOTAL_MOVIE_TO_DISPLAY]
    for each in data:
        item = dict()
        item['title'] = each['title']
        item['storyline'] = each['overview']
        item['poster'] = IMG_PATH + each['poster_path']
        item['trailer'] = get_trailer(each['id'])
        output_list.append(item)
    return output_list


# Call the data generating function to movie data generation from API
movies = []
movies_data_list = get_details()

# Create Instances of Movie Class
for each in movies_data_list:
    movie = media.Movie(
        each['title'],
        each['storyline'],
        each['poster'],
        each['trailer'])
    movies.append(movie)

# Generate HTML file
fresh_tomatoes.open_movies_page(movies)
