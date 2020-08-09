from django.urls import path
from . import views
urlpatterns = [
    # path('', views.index,name="index"),
    path('', views.home,name="home"),
    path('dashboard', views.dashboard,name="dashboard"),
    path('search', views.search,name="search"),
    path('search/book', views.book,name="book"),
    path('addbook', views.addbook,name="addbook"),
    path('history', views.history,name="history"),
    path('notification', views.notification,name="notification"),
    path('account', views.account,name="account"),

]