from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('create/', views.create, name="create"),
    path('new/', views.new, name="new"),
    path('complete/', views.complete, name="complete"),
]
