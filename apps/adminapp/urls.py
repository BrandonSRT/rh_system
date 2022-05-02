from django.urls import path
from django.contrib.auth.decorators import login_required
from ..commonapp.decorators import allowed_users
from . import views


urlpatterns = [
    path("",login_required(login_url='Login')
         (allowed_users(allowed_roles=['admin'])
          ( views.search.as_view())), name="search"),
    path("register_user", login_required(login_url='Login')
         (allowed_users(allowed_roles=['admin'])
          ( views.register_user.as_view())), name="register_user"),
    path("form_attached/<pk>", login_required(login_url='Login')
         (allowed_users(allowed_roles=['admin'])
          ( views.form_attached.as_view())), name="form_attached"),


]