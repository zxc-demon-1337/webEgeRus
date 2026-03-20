from django.shortcuts import render

# Create your views here.

def training_home(request):
    return render(request, 'training/training_home.html')