from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


# Create your views here.
def index(request):
    return HttpResponse("StockApp")

def goods(request, gid):
    if(request.GET):
        print(request.GET)
    return HttpResponse(f"Goods {gid}")

def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=True)

    return HttpResponse(f"faas {year}")


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')