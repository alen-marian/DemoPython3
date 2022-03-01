from django.http import HttpResponse
from django.shortcuts import render
from . models import Place, People

# Create your views here.


def demo(request):
    obj = Place.objects.all()
    obj1 = People.objects.all()
    return render(request, "index.html", {'result': obj, 'result1': obj1})


# addition(request):
    #x = int(request.GET['num1'])
   # return render(request, "result.html", {'addition': add, 'substraction': sub, 'division': div, 'multiply': mul})
