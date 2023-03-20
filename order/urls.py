from django.urls import path, include
from . import views

urlpatterns = [
    # path("", views.home, name='home'),
    path("", views.ItemView.as_view(), name="items"),
    path("item/<int:pk>/", views.DetailView.as_view(), name="detail"),
    path('add-item/', views.CreateView.as_view(), name='add-item'),
    path('delete-item/<int:pk>/', views.DeleteView.as_view(), name='delete-item'),

]
