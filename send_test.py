from multiprocessing.sharedctypes import Value
import time
import requests
import json
from requests import Request
import os

os.environ["CUDA_VISIBLE_DEVICES"]=""

# movie_map = {
#     "movieName": {
#       "Toy Story (1995)": 5,
#       "Taxi Driver (1976)": 3,
#       "GoldenEye (1995)": 4
#     },
#     "movieCount": 5
# }

# Test 1
movie_map = {
    "movieName": {
      1: 5,
      23: 3,
      2: 4
    },
    "movieCount": 5
}

# Test 2: Star wars issue resolved
# movie_map = {
#     "movieName": {
#       "50": 5,
#       "719": 3
#     },
#     "movieCount": 5
# }

json_movie_map = json.dumps(movie_map)
response = requests.post("https://hxudmk07fj.execute-api.us-east-1.amazonaws.com/default/MovieRecommendation", json=json_movie_map)
print(response.json())