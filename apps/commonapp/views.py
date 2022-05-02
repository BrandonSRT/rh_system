from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required, user_passes_test
from.decorators import unauthenticated_user
from apps.commonapp.decorators import unauthenticated_user
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib import messages

# Create your views here.
# class (View):
#     def get(self, request):

#         return render(request, "common/Layout.html")
class Login(View):
    @method_decorator(unauthenticated_user())

    def get(self, request):

        return render(request, "common/main.html")

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('search')
        else:
            messages.error(request, 'Usuario o Contraseña incorrecta')

        context = {}         
        return render(request, "common/main.html", context)


class logout_view(View):
    @method_decorator(login_required(login_url='login'))
    def get(self, request):
        logout(request)
        return redirect('Login')   