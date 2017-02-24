from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Index page of buyer application")


def dish(request, dish_id):
    return HttpResponse("You're looking at dish %s" % dish_id)


def dish(request, ingredient_id):
    return HttpResponse("You're looking at ingredient %s" % ingredient_id)