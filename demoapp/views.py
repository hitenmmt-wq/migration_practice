from django.shortcuts import render
from django.utils import timezone

# Create your views here.


def get_user(request):
    user = request.user
    print("user ", user)
    return user
  
def get_dashboard(data):
    today = timezone.now().date()
    cate_data = {
        "data": data,
        "date": today,
    }
    return cate_data
