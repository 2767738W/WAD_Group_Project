from django.shortcuts import render
from django.http import HttpResponse
from wad.forms import UserForm, UserProfileForm
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def home(request):
    #code for getting most liked recipies in here
    return render(request, 'project/home.html')

def user_login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:

                login(request, user)
                return redirect(reverse('project:home'))
            else:
                return HttpResponse("Your account is disabled.")
        else:

            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("invalid login details supplied.")
        
    else:
        return render(request, 'project/login.html')

@login_required
def user_logout(request):
    #user is already logged in so we can log them out
    logout(request)
    #take user back to homepage
    return redirect(reverse('project:home'))


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
