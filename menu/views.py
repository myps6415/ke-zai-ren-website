from django.shortcuts import render
from datetime import datetime
from .models import menu

# Create your views here.
def hello_view(request):
    return render(request, 'hello_django.html', {
        'current_time': str(datetime.now()),
    })


def menus(request):
    menu_list = menu.objects.all()
    return render(request, 'menu.html', {
        'post_list': menu_list, })