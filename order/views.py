from django.shortcuts import render, redirect
from .models import Orders
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


@login_required()
def home(request):
    return render(request, 'order/home.html')

@login_required()
def tags(request, slug):
    order = Orders.objects.filter(tags = slug).values()
    context = {
        'order':order
    }
    print()
    return render(request, 'order/tags.html', context=context)

class OrderView(LoginRequiredMixin, generic.ListView):
    context_object_name = 'Orders'
    template_name = 'order/orders_list.html'

    def get_queryset(self):
        return Orders.objects.all()

class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Orders
    context_object_name = 'order'
    template_name = 'order/detail.html'

class UpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Orders
    context_object_name = 'order'
    template_name = 'order/edit.html'
    fields = ['name', 'description', 'price', 'quantity', 'favorites', 'tags']
    
    def form_valid(self, form):
        form.instance.date_updated = timezone.now()
        return super().form_valid(form)
    
class CreateView(LoginRequiredMixin, generic.CreateView):
    model = Orders
    context_object_name = 'order'
    success_url = ''
    success_message = "Order created successfully"
    template_name = 'order/add.html'
    fields = ['name', 'description', 'price', 'quantity', 'favorites', 'tags']

    def form_valid(self, form):
        form.instance.date_updated = timezone.now()
        return super().form_valid(form)


class DeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Orders
    success_url = '/'
    success_message = "Order deleted successfully"


    def delete(self, request, *args, **kwargs):
        return super(DeleteView, self).delete(request, *args, **kwargs)
    template_name = 'order/delete.html'

@login_required()
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

