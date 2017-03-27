from django.shortcuts import render
from django.http import HttpResponse
from .models import Dish


def index(request):
    return HttpResponse("Index page of buyer application")


def dish(request, dish_id):
    return HttpResponse("You're looking at dish %s" % dish_id)


def dish_list(request):
    data = {}
    categories = Dish.CATEGORY_CHOICES
    dishes = Dish.objects.all()
    for key, value in categories:
        data[value] = []

    for the_dish in dishes:
        data[the_dish.get_category_display()].append(the_dish)
    new_data = {}

    for key in data:
        if len(data[key]) != 0:
            new_data[key] = data[key]

    return render(request, 'buyer/dish_list.html', {'new_data': new_data})
