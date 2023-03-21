from django.shortcuts import render, redirect
from .models import Orders
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from .forms import UserRegisterForm

def home(request):
    return render(request, 'order/home.html')

class OrderView(generic.ListView):
    context_object_name = 'Orders'
    template_name = 'order/items_list.html'

    def get_queryset(self):
        return Orders.objects.all()

class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Orders
    context_object_name = 'order'
    template_name = 'order/detail.html'

class UpdateView(generic.UpdateView):
    model = Orders
    context_object_name = 'order'
    template_name = 'order/edit.html'
    fields = ['name', 'description', 'price', 'quantity', 'favorites']
    
    def form_valid(self, form):
        form.instance.date_updated = timezone.now()
        return super().form_valid(form)
    
class CreateView(generic.CreateView):
    model = Orders
    context_object_name = 'order'
    success_url = ''
    success_message = "Order created successfully"
    template_name = 'order/add.html'
    fields = ['name', 'description', 'price', 'quantity', 'favorites']

    def form_valid(self, form):
        form.instance.date_updated = timezone.now()
        return super().form_valid(form)


class DeleteView(generic.DeleteView):
    model = Orders
    success_url = '/'
    success_message = "Order deleted successfully"


    def delete(self, request, *args, **kwargs):
        return super(DeleteView, self).delete(request, *args, **kwargs)
    template_name = 'order/delete.html'

def favorites(request):
    list = []
    for order in Orders.objects.all():
        if order.favorites == True:
            list.append(order)
    context = {'order':list}
    return render(request, 'order/favorites_order.html', context=context)


# login system

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('orders')
    else:
        form = UserRegisterForm()
    return render(request, 'order/register.html', {'form' : form})

