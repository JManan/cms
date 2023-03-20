from django.shortcuts import render, redirect
from .models import Items
from django.views import generic
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

def home(request):
    return render(request, 'order/home.html')

class ItemView(generic.ListView):
    context_object_name = 'Items'
    template_name = 'order/items_list.html'

    def get_queryset(self):
        return Items.objects.all()

class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Items
    context_object_name = 'item'
    template_name = 'order/detail.html'
