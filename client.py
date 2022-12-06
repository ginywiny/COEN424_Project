from multiprocessing.sharedctypes import Value
from difflib import get_close_matches, SequenceMatcher
import json
import requests

# Dict to be converted as JSON body for request
movie_map = {}
movie_map["movieName"] = {}
movie_list = list()
map_id = {}
json_response = {}

# Create list of all movies
def createMovieList():
    global movie_list
    file = open("MovieList.txt", "r")
    data = file.read()
    movie_list = data.split("\n")
    createMovieIDMap(movie_list)

# Create ID mapping for all movies
def createMovieIDMap(movies):
    global map_id
    for i in range(0, len(movies)):
        map_id[movies[i]] = i + 1 # Base 1 not 0
        
# Get the full name of the entered movie name
def findFullName(movie):
    global movie_list
    full_name = get_close_matches(movie, movie_list, n=1, cutoff=0)[0] # Get 1 name with minimum 60% accuracy
    print("Closest movie found: ", full_name)
    return full_name

# Get the ID from the movie mapping
def getMovieID(movie) :
    return map_id[movie]

# Get the user input for the movies, ratings and wanted prediction
def getUserMovies():
    # Input movie name and rating
    global movie_map
    print("Please select movie names and their rating [1 (low) to 5 (high)]...")
    print()
    while True:
        # Take movie name
        movie_name = ""
        while True:
            movie_name = input("Write movie name and hit enter: ")
            movie_name = findFullName(movie_name) # Get full movie name if not exactly written
            movie_name_ID = getMovieID(movie_name)
            
            # Check if movie already entered
            if (movie_name_ID in movie_map["movieName"]):
                print("ERROR: Movie already entered! Try again...")
            else:
                # movie_name = findFullName(movie_name)
                break

        # Take movie rating
        movie_rating = ""
        while True:
            movie_rating = input("Write movie rating between 1 to 5 and hit enter: ")
            
            # Check if value is an integer            
            try:
                movie_rating = int(movie_rating)
            except ValueError:
                print("ERROR: Invalid rating entered! Try again...")
                continue

            # Check if number between 1 and 5
            if (movie_rating >= 1 and movie_rating <= 5):
                break
            else:
                print("ERROR: Invalid rating entered! Try again...")
            
        print("Movie and Rating: ", movie_name, " ID:", movie_name_ID, " Rating:" , movie_rating)
        print()
        movie_map["movieName"][movie_name_ID] = movie_rating
        
        # Is done selecting movies
        done = input("Done selecting movies? y/n: ")
        if (done == "y"):
            break
    
    # Input movie recommendation count
    print()
    movie_count = 1
    while True:
        movie_count = input("Select number of movies to recommend [1 to 1692]: " )
        # Check if value is an integer            
        try:
            movie_count = int(movie_count)
        except ValueError:
            continue

        # Check if number between 1 and 5
        if (movie_count >= 1 and movie_count <= 1692):
            break
        
    movie_map["movieCount"] = movie_count
    print("Predicting recommendations...")
    
# POST request and receive response for prediction of recommendations
def sendRequest():
    # Issue API POST request for recommendations
    json_movie_map = json.dumps(movie_map)
    json_response = requests.post("https://hxudmk07fj.execute-api.us-east-1.amazonaws.com/default/MovieRecommendation", json=json_movie_map)
    json_response = json_response.json()
    return json_response["movie_recommendation"] 

if __name__ == "__main__":
    # Get list of movies and create mapping
    createMovieList()
    
    # Get user input for prediction
    getUserMovies()
    
    # Send request for movie predictions 
    recommendation = sendRequest()
    print("Recommended movies in order of preference...")
    print("---------------------------------------------")
    for i in range(0, len(recommendation)):
        print(i + 1, ":", recommendation[i])
    print("---------------------------------------------")
    