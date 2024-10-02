from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Transport Management System!")

from django.shortcuts import render

def vehicle_list(request):
    # Your logic here
    return render(request, 'vehicle_list.html')

def vehicle_create(request):
    # Your logic here
    return render(request, 'vehicle_create.html')

def vehicle_update(request, id):
    # Your logic here
    return render(request, 'vehicle_update.html')

def vehicle_delete(request, id):
    # Your logic here
    return render(request, 'vehicle_delete.html')
