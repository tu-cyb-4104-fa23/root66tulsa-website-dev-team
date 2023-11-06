from django.urls import path
from front_end import views

app_name = 'front_end'

urlpatterns = [
    path("", views.index, name='index'),
]