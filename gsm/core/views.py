from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, response


def index(request):
    # response["Access-Control-Allow-Origin"] = "*"
    # response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    # response["Access-Control-Max-Age"] = "1000"
    # response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return render(request, 'index.html')
