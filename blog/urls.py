from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^about/', views.about, name='about'),
    url(r'^sitemap/', views.sitemap, name='sitemap'),
    url(r'^list_all_posts/', views.list_all_posts, name='list_all_posts'),
    url(r'^$', views.blog, name='blog'),
    url(r'^(?P<slug>[^/]+)/$', views.readblog, name='readblog'),

]










