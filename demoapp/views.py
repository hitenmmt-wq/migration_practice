from django.shortcuts import render

# Create your views here.


def get_user(request):
    user = request.user
    print("user ", user)
    return user
