from django.shortcuts import render, redirect
from .models import Items
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone


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


class CreateView(generic.CreateView):
    model = Items
    context_object_name = 'item'
    success_url = ''
    success_message = "Post created successfully"
    template_name = 'order/add.html'
    fields = ['name', 'description', 'price', 'quantity']

    def form_valid(self, form):
        form.instance.date_updated = timezone.now()
        return super().form_valid(form)


class DeleteView(generic.DeleteView):
    model = Items
    success_url = '/'
    success_message = "Item deleted successfully"


    def delete(self, request, *args, **kwargs):
        return super(DeleteView, self).delete(request, *args, **kwargs)
    template_name = 'order/delete.html'