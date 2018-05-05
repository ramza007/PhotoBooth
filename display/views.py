from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from display import urls
from .models import Images

# Create your views here.


def welcome(request):
    return render (request, 'welcome.html')


def display_image(request):
    date = dt.date.today()
    return render(request, 'today.html', {"date": date})


def single_photo(request, photo_id):
    photo = Images.objects.get(id=photo_id)
    return render(request, 'single_image.html', {'photo': photo})
