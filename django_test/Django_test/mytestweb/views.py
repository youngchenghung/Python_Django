from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
import datetime

# Create your views here.

def index(request):
    web_name = "Leo Django web site"
    article_list = [{'title':"Django web site", 'author':"Leo", 'date':datetime.datetime.strptime("2024-04-27", "%Y-%m-%d")},
                    {'title':"test web site 1", 'author':"Tom", 'date':datetime.datetime.strptime("2024-04-28", "%Y-%m-%d")},
                    {'title':"test web site 2", 'author':"Jack", 'date':datetime.datetime.strptime("2024-04-29", "%Y-%m-%d")},]
    return render(request, 'home_page.html', context={'web_name':web_name, 'article_list':article_list})

def dict_http(request):
    list_1 = [{'a':"1", 'b':"2", 'c':"3", 'd':"4", 'e':"5"},
              {'f':"6", 'g':"7", 'h':"8", 'i':"9", 'j':"10"},
              {'一':"1", '二':"2", '三':"3", '四':"4", '五':"5"}]
    str1js = json.dumps(list_1)
    return HttpResponse(str1js)

def dict_json(request):
    list_1 = [{'a':"1", 'b':"2", 'c':"3", 'd':"4", 'e':"5"},
              {'f':"6", 'g':"7", 'h':"8", 'i':"9", 'j':"10"},
              {'一':"1", '二':"2", '三':"3", '四':"4", '五':"5"}]
    return JsonResponse(list_1, safe=False)

def hello_view(request):
    return render(request, 'hello_django.html',{'data':'Hello Django!',})