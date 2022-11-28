from multiprocessing.sharedctypes import Value
import time
import requests
from requests import Request

movie_map = {}


print("Please enter movie name and its rating from 1 to 5...")
while True:
    
    # # TODO: Fix this bullshit for some reason import is not working
    # # Break loop if done
    # print("Press esc if done inputting movies...")
    # if keyboard.is_pressed('esc'):
    #     break
    # time.sleep(0.1)
    
    done = input("Done selecting movies? y/n: ")
    if (done == "y"):
        break
    
    # Take movie name
    movie_name = ""
    while True:
        movie_name = input("Write movie name and hit enter: ")
        
        # Check if movie already entered
        if (movie_name in movie_map):
            print("Movie already entered! Try again...")
        else:
            break
        # TODO: Logic to handle if movie exists in list

    # Take movie rating
    movie_rating = ""
    while True:
        movie_rating = input("Write movie rating between 1 to 5 and hit enter: ")
        
        # Check if value is an integer            
        try:
            movie_rating = int(movie_rating)
        except ValueError:
            continue

        # Check if number between 1 and 5
        if (movie_rating >= 1 and movie_rating <= 5):
            break
            
    print("Movie and Rating: ", movie_name, " ", movie_rating)
    movie_map[movie_name] = movie_rating
    
# POST: https://hxudmk07fj.execute-api.us-east-1.amazonaws.com/default/MovieRecommendation?movieName=Michael
r = Request('POST', 'https://myurl.com', headers={'hello': 'world'}, json=movie_map)
x = r.prepare()
# x.headers{'hello': 'world', 'Content-Length': '16', 'Content-Type': 'application/json'}

# print(movie_map)
    
