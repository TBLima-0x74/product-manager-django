from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("produtos/", views.produtos, name="produtos"),
    path("user/<username>/", views.user, name="user"),
]
