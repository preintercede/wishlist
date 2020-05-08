from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.views.generic.edit import CreateView,DeleteView

# Create your views here.
def home(request):
    item_list = Item.objects.all()
    return render(request, 'home.html', {'items': item_list})

class AddList(CreateView):
    model = Item
    fields = ['description']
    success_url = '/'

class ItemDelete(DeleteView):
    model = Item
    success_url = '/'