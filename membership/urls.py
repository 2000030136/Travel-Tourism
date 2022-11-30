from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    # path('memberdetails/', views.memberdetails, name='memberdetails'),
    # path('viewmemberdetails/', views.viewmemberdetails, name='view'),
    path('addmember/',views.addmember,name='addmember'),
    path('login/',views.login,name='login'),
    path('', views.register, name='register'),
    path('piechart/',views.piechart,name='piechart')
]