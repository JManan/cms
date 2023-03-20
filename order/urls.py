from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("items/", views.ItemView.as_view(), name="items"),
    path("item/<int:pk>/", views.DetailView.as_view(), name="detail"),
]
