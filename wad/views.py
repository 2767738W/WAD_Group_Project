from django.shortcuts import render
from django.http import HttpResponse
from wad.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.urls import reverse

def home(request):
    return render(request, 'project/home.html')

def register(request):
    
    registered = False

    if request.method == 'POST':
        
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
           
            profile.save()

            registered = True
        else:
            
            print(user_form.errors, profile_form.errors)
    else:
        
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'project/register.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    })
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('project/base.html'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'project/login.html')
