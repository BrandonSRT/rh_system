from django.urls import path
from . import views


urlpatterns = [
    path("", views.Login.as_view(), name="Login"),
    path("logout/", views.logout_view.as_view(), name="logout"),

]