from django.contrib import admin
from django.urls import path
from tvapp import views

urlpatterns = [
    path("", views.home, name='home'),
    path("netflix", views.netflix, name='netflix'),
    # Go to homepage
    path("home", views.base, name='base'),
    path("top1-10", views.top10, name='top1-10'),
    path("top11-20", views.top20, name='top11-20'),
    path("recommend", views.recommend, name='recommend'),
    path("rec11-20", views.rec11_20, name='rec11-20'),
    path("rec21-30", views.rec21_30, name='rec21-30'),
    path("rec31-40", views.rec31_40, name='rec31-40'),
    path("rec41-50", views.rec41_50, name='rec41-50'),
    path("rec51-58", views.rec51_58, name='rec51-58'),
    path("action", views.action, name='action'),
    path("adventure", views.adventure, name='adventure'),
    path("comedy", views.comedy, name='comedy'),
    path("horror", views.horror, name='horror'),
    path("history", views.history, name='history'),
    path("documentary", views.documentary, name='documentary'),
    path("drama", views.drama, name='drama'),
    path("sci_fi", views.sci_fi, name='sci_fi')
]
