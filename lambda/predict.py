import torch

def predict(movieName):
    model = torch.load('model.pt')
