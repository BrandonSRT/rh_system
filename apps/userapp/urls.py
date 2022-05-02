from django.urls import path
from django.contrib.auth.decorators import login_required
from ..commonapp.decorators import allowed_users
from . import views


urlpatterns = [
    path("candidate", views.candidateForm.as_view(), name="candidate"),
    path("candidate_edit/<pk>",login_required(login_url='Login')
         (allowed_users(allowed_roles=['admin'])
          ( views.candidateFormedit.as_view())), name="candidate_edit"),
    path('candidate_delete/<int:id>',login_required(login_url='Login')
         (allowed_users(allowed_roles=['admin'])
          ( views.candidate_delete)), name="candidate_delete"),

]