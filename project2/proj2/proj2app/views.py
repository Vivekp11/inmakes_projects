from django.shortcuts import render
from . models import place
from . models import profile
# Create your views here.
def home(request):
    obj = place.objects.all()
    obj1 = profile.objects.all()
    return render(request, 'index.html', {'result': obj, 'result1': obj1})

