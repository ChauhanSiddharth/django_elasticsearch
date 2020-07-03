from django.shortcuts import render
from .documents import CarDocument
from eapp.models import Car

# Create your views here.
def search(request):
    q = request.GET.get('q')
    all_cars = Car.objects.all()
    if q:
        # cars = CarDocument.search().query("match", name=q)
        cars = CarDocument.search().query('multi_match', query=q,fields=['name', 'description','color'])
    else:
        cars = ''

    return render(request, 'find.html', {'cars': cars,'allcars':all_cars})