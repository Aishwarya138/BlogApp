from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('post/<str:pk>', views.post, name='post'),
  path('addblog', views.addblog, name='addblog'),
  path('addblogdisplay', views.addblogdisplay, name='addblogdisplay'),
  path('deleteblog', views.deleteblog, name='deleteblog'),
  path('deleteblogdisplay', views.deleteblogdisplay, name='deleteblogdisplay')
  ]