from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'base.html')

def create_recorded_time(request):
    return render(request, 'base.html')