from django.shortcuts import render
from django.http import HttpResponse, response


# Create your views here.

def index(requeset):
    return HttpResponse("Hello world, you're at the polls index")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
