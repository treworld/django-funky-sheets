from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/', views.CreateMovieView.as_view(), name='create'),
    url(r'^update/', views.UpdateMovieView.as_view(), name='update'),
]
