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
    # print("My request",request)         United Nations
    country1 = request.GET['country']   # United
    # print("Country name", country1)
    capital1 = request.GET['capital']     
    actualcapital = request.GET['actualcapital']
    # print("Country name", actualcapital)
    if capital1.lower()==actualcapital.lower():
        return render(request,'result.html',{'country1':country1, 'resCorrect':"Your Answer is Correct", 'resInCorrect':""})
    else:
        return render(request,'result.html',{'country1':country1, 'resCorrect':"", 'resInCorrect':"The correct answer is:"+actualcapital})
