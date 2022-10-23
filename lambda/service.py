# -*- coding: utf-8 -*-
import torch
import os

def handler(event, context):
    # Your code goes here!
    e = event.get('e')
    pi = event.get('pi')
    return {
        "statusCode": 200,
        "headers": { "Content-Type": "application/json"},
        "body": e + pi
    }