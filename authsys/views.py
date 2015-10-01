from django.shortcuts import render
from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import redirect

def login(request):
    params = {}
    params.update(csrf(request))
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            request.session['authinfo']='ok'
            return redirect('/')
        else:
            request.session['authinfo']='User not found'
            return redirect('/')
    return  redirect('/')

def logout(request):
    auth.logout(request)
    return redirect('/')

