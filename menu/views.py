from django.shortcuts import render
from datetime import datetime


# Create your views here.
def hello_view(request):
    return render(request, 'hello_django.html', {
        'current_time': str(datetime.now()),
    })