# from django.conf.urls import url
# from . import views
#
# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     url(r'^login/$', views.login, name='login'),
#     url(r'^home/$', views.home, name='home'),
# ]
#
# # from django.urls import path
# # from . import views
# # urlpatterns=[
# #     path("",views.index,name="index"),
# #     path("render/",views.load,name='load'),
# # ]
from django.urls import path
from . import views
urlpatterns = [
    path('base/', views.index),
    path('login/', views.login),
    path('home/', views.home),
]