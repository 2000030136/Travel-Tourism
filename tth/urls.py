# from django.urls import path
# from . import views
# urlpatterns=[
#     path("",views.index,name="index"),
#     path("render/",views.load,name='load'),
# ]
from django.urls import path
from . import views


urlpatterns = [

    path('index/', views.index),
    path('basic/', views.basic),
    path('register/', views.register),
    path('tours/', views.tours),
    path('contact/', views.contact),
    path('cards/', views.cards),
    path('payment/', views.payment),
    path('australia/', views.australia),

]
