from django.contrib import admin
from django.urls import path
from firstapp import views
app_name = 'myapp'
urlpatterns = [

    path('',views.index),
    path('book/<int:book_id>/',views.detail, name = 'detail'),
]
