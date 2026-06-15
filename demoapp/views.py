from django.shortcuts import render
from django.utils import timezone

# Create your views here.


def get_dashboard(data):
    today = timezone.now().date()
    cate_data = {
        "data": data,
        "date": today,
    }
    return cate_data