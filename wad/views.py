from django.shortcuts import render
from django.http import HttpResponse
from wad.forms import UserForm, UserProfileForm

def home(request):
    return render(request, 'project/home.html')

def user_login(request):
    return render(request, 'project/login.html')

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

    return render(request, 'wad/register.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    })
