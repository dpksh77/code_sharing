from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^time/', views.time, name='time'),
    url(r'^user/(?P<username>[A-Za-z0-9]+)/$', views.profile, name='profile'),
    url(r'^books/$', views.books_catagory ,name="books"),
    url(r'^books/(?P<catagory>[\w-]+)/$', views.books_catagory,name="books"),
]