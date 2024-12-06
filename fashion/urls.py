from django.urls import path
from . import views
urlpatterns = [
    path("", views.main, name="main"),
    path("fashion/", views.fashion, name="fashion"),
    path('fashion/details/<int:id>', views.details, name='details'),

]