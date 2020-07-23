from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name="index"),
    path('home/', views.home,name="home"),
    path('home/dashboard', views.dashboard,name="dashboard"),
    path('home/search', views.search,name="search"),
    path('home/search/book', views.book,name="book"),
    path('home/history', views.history,name="history"),
    path('home/notification', views.notification,name="notification"),
    path('home/account', views.account,name="account"),

]