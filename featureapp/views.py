from django.shortcuts import render

# Create your views here.

def calculate_round_data(value):
    data = round(value, 2)
    return data
