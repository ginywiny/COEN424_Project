from multiprocessing.sharedctypes import Value
import time
import requests
import json
from requests import Request

movie_map = {}
movie_map["Toy Story"] = 5
movie_map["Cars"] = 3

json_movie_map = json.dumps(movie_map)
path = 'https://hxudmk07fj.execute-api.us-east-1.amazonaws.com/default/MovieRecommendation?movieName=', json_movie_map


# r = Request('POST', 'https://hxudmk07fj.execute-api.us-east-1.amazonaws.com/default/MovieRecommendation?movieName=',json_movie_map, json=movie_map)

# TODO: Update to handle POST and GET based on specific endpoints (POST movies, GET recommendations...)
response = requests.post("https://hxudmk07fj.execute-api.us-east-1.amazonaws.com/default/MovieRecommendation", json=json_movie_map)
# response = requests.post(path)
print(response.json())