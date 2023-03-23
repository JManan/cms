from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.OrderView.as_view(), name="orders"),
    path("order/<int:pk>/", views.DetailView.as_view(), name="detail"),
    path('add-order/', views.CreateView.as_view(), name='add-order'),
    path('delete-order/<int:pk>/', views.DeleteView.as_view(), name='delete-order'),
    path('edit/<int:pk>/', views.UpdateView.as_view(), name='edit-post'),
    path('login/', auth_views.LoginView.as_view(template_name='order/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='order/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('favorites/', views.favorites, name='favorites'),
    path('order/<slug:slug>/', views.tags, name='tags'),
]
