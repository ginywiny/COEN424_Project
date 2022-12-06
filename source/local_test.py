from multiprocessing.sharedctypes import Value
import inference as inference

dict_test = {
    "1": 5,
    "23": 3,
    "2":  4
}

# movie_map = {
#     "movieName": {
#       "1": 5,
#       "23": 3,
#       "2": 4
#     },
#     "movieCount": 5
# }

print(inference.infer(dict_test, 5))