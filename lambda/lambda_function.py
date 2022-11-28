# -*- coding: utf-8 -*-
import torch
import os
import json

def lambda_handler(event, context):
    # Your code goes here!
    movie_name = ""
    error_message = ""
    print(event)
    
    
    # Body mow contains the request
    try:
        movie_dict_json = event["body"]
        movie_dict = json.loads(movie_dict_json)
    except:
        error_message = "POST request body empty"
        
    if error_message != "":
        return {
            "statusCode": 400,
            "headers": { "Content-Type": "application/json" },
            "body": json.dumps(error_message)
        }
    else:
        return {
            "statusCode": 200,
            "headers": { "Content-Type": "application/json"},
            "body": json.dumps(movie_dict)
        }
    
    
    # # Used for MovieName
    # try:
    #     movie_name = event["queryStringParameters"]["movieName"]
    # except:
    #     error_message = "expected movieName parameter but got null"
    # if error_message != "":
    #     return {
    #         "statusCode": 400,
    #         "headers": { "Content-Type": "application/json" },
    #         "body": json.dumps(error_message)
    #     }
    # else:
    #     return {
    #         "statusCode": 200,
    #         "headers": { "Content-Type": "application/json"},
    #         "body": json.dumps(movie_name)
    #     }