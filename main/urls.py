from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.index, name='index'),
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
]
# Int:id - means that it's going to search for integers in the url, and it will pass it to the function view.index
