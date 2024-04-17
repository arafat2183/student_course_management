from django.http import HttpResponse
from django.shortcuts import render


def studentView(request):
    return HttpResponse("Hello, Students!")
