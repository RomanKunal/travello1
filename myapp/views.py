from django.shortcuts import render
from .models import Destination
def index(request):
    dest1=Destination()
    dest1.name="Mumbai"
    dest1.desc="The city that can't sleep"
    dest1.img="destination_10.jfif"
    dest1.price="From Rs 70"

    dest2=Destination()
    dest2.name="Delhi"
    dest2.desc="The city of forts"
    dest2.img="destination_7.jpg"
    dest2.price="From Rs 80"
    
    dest3=Destination()
    dest3.name="Bangalore"
    dest3.desc="The city of gardens"
    dest3.img="destination_8.jpg"
    dest3.price="From Rs 90"
    data=[dest1,dest2,dest3]
    return render(request, 'index.html',{'dests':data})


    