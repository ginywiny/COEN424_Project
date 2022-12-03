# -*- coding: utf-8 -*-
import torch
import os
import json
import ml.GNN_new.inference as inference

def lambda_handler(event, context):
    error_message = ""
    print(event)
    
    # Body now contains the request
    try:
        # Body: Movies watched (dict with their rating) and movies to recommend
        # Load json to dict
        body = event["body"]
        json_body = json.loads(body)
        print("CONVERTED BODY: ", json_body)
        try:
            print(type(json_body))
            json_body = json.loads(json_body)
            print(json_body.keys())
        except:
            print("JSON mapping not referenced")
        
        # Get movies and prediction count
        dict_body_movies = json_body["movieName"]
        body_prediction_count = json_body["movieCount"]
        # print("movies: ", dict_body_movies)
        # print("prediction count movies: ", body_prediction_count)
    except:
        error_message = "POST request body empty"
        
    # If message is empty and no movies are given
    if error_message != "":
        response_object = {}
        response_object["statusCode"] = 400
        response_object["headers"] = {}
        response_object["headers"]["Content-Type"] = "application/json"
        response_object["body"] = json.dumps(error_message)
        return response_object
        # return {
        #     "statusCode": 400,
        #     "headers": { "Content-Type": "application/json" },
        #     "body": json.dumps(error_message)
        # }
        
    # If message body has movies
    else:
        # Convert the movies names to their respective number IDs 
        final_dict = {}
        # TODO: When making the UI, USE THE SPECIFIC MOVIE ID INSTEAD OF RECONVERTING!
        for key, value in dict_body_movies.items():
            title_id = inference.title_to_id(key)
            final_dict[title_id] = value
        recommended_movies = inference.infer(final_dict, body_prediction_count)
        
        # Movie JSON object
        movie_response = {}
        movie_response["movies_selected"] = dict_body_movies
        movie_response["movie_prediction_count"] = body_prediction_count
        movie_response["movie_recommendation"] = recommended_movies
        
        # Response object
        response_object = {}
        response_object["statusCode"] = 200
        response_object["headers"] = {}
        response_object["headers"]["Content-Type"] = "application/json"
        response_object["body"] = json.dumps(movie_response)
        # response_object["body"] = json.dumps(json_body)
        return response_object