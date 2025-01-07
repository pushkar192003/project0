from django.shortcuts import render
from django.http import HttpResponse  
from .models import Flight
# Create your views here.





def flight_list(request):
    flights = Flight.objects.all()
    return render(request, 'flights/flight_list.html', {'flights': flights})
