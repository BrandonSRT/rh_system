from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user():
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect('search')
            else:
                return func(request, *args, **kwargs)
        return wrapper
    return decorator

def allowed_users(allowed_roles=[]):
    def decorator(func):
        def wrapper(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to see this page')
        return wrapper
    return decorator

def admin_only():
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group == 'customer':    
                return redirect('gerente')

            if group == 'admin':    
                return func(request, *args, **kwargs)
        return wrapper
    return decorator



