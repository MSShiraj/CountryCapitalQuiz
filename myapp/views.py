from django.shortcuts import render
import requests
from django.db.models.aggregates import Count
from random import randint

# Create your views here.

def home(request):
    response=requests.get('https://countriesnow.space/api/v0.1/countries/capital').json()
     
    #number=response[1]
    # count = aggregate(count=Count('id'))['count']
    # random_index = randint(0, count - 1)
    data= response['data']
    index=randint(0,len(data)-1)

    obj= data[index]
    return render(request,'home.html',{'response':obj})

def check(request):
    print("My request",request)
    country1 = request.GET['country']
    capital1 = request.GET['capital']
    actualcapital = request.GET['actualcapital']
    print("Checked")
    if capital1.lower()==actualcapital.lower():
        return render(request,'result.html',{'country1':country1, 'resCorrect':actualcapital, 'resInCorrect':""})
    else:
        return render(request,'result.html',{'country1':country1, 'resCorrect':"", 'resInCorrect':actualcapital})