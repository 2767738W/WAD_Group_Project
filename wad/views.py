from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from wad.forms import RecipeForm, UserForm, UserProfileForm
from wad.models import Recipe, UserProfile, starRating


def home(request):
    top_ten_recipes = Recipe.objects.annotate(avg_rating=Avg('starrating__rating')).order_by('-avg_rating')[:10]
    return render(request, 'project/home.html', {'recipes': top_ten_recipes})


class CuisineView(View):
    def get(self, request):
        return render(request, 'project/Cuisine.html')


class ItalianView(View):
    def get(self, request):
        context_dict = {}
        try:
            italian_recipes = Recipe.objects.filter(cuisine='italian')
            context_dict['recipes'] = italian_recipes
        except Recipe.DoesNotExist:
            context_dict['recipes'] = None

        return render(request, 'project/italian.html', context=context_dict)


class ChineseView(View):
    def get(self, request):
        context_dict = {}
        
        try:
            chinese_recipes = Recipe.objects.filter(cuisine='chinese')
            context_dict['recipes'] = chinese_recipes
        except Recipe.DoesNotExist:
            context_dict['recipes'] = None

        return render(request, 'project/chinese.html', context=context_dict)


class ThaiView(View):
    def get(self, request):
        context_dict = {}
        try:
            thai_recipes = Recipe.objects.filter(cuisine='thai')
            context_dict['recipes'] = thai_recipes
        except Recipe.DoesNotExist:
            context_dict['recipes'] = None

        return render(request, 'project/thai.html', context=context_dict)
        

class IndianView(View):
    def get(self, request):
        context_dict = {}
        try:
            indian_recipes = Recipe.objects.filter(cuisine='indian')
            context_dict['recipes'] = indian_recipes
        except Recipe.DoesNotExist:
            context_dict['recipes'] = None

        return render(request, 'project/indian.html', context=context_dict)
        
        
class AddRecipeView(View):
    template_name = 'project/AddRecipe.html'

    def get(self, request):
        form = RecipeForm()
        top_ten_recipes = Recipe.objects.annotate(avg_rating=Avg('starrating__rating')).order_by('-avg_rating')[:10]
        return render(request, 'project/AddRecipe.html', {'form': form, 'recipes': top_ten_recipes})

    def post(self, request):
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            
            if request.user.is_authenticated:
                user_profile = request.user.userprofile
                recipe.user = user_profile
            
            recipe.save()

            return redirect(reverse('wad:view_recipe', kwargs={'cuisine_name': recipe.cuisine, 'recipe_name_slug': recipe.slug}))
        else:
            top_ten_recipes = Recipe.objects.annotate(avg_rating=Avg('starrating__rating')).order_by('-avg_rating')[:10]
            return render(request, 'project/AddRecipe.html', {'form': form, 'recipes': top_ten_recipes})


class ViewRecipeView(View):
    def get(self, request, cuisine_name, recipe_name_slug):
        context_dict = {}
        
        cuisine_choices = [choice[0] for choice in Recipe.CUISINE_CHOICES]

        try:
            if cuisine_name in cuisine_choices:
                recipe = Recipe.objects.get(slug=recipe_name_slug, cuisine=cuisine_name)
                context_dict['recipe'] = recipe
                context_dict['cuisine_name'] = cuisine_name
            else:
                context_dict['cuisine_name'] = None
        except Recipe.DoesNotExist:
            context_dict['recipe'] = None

        return render(request, 'project/ViewRecipe.html', context=context_dict)
    
        
class UserLoginView(View):
    def get(self, request):
        return render(request, 'project/login.html')

    def post(self, request):
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('wad:home'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied. Return to the login page <a href='{}'>here</a>.".format(reverse('wad:login')))


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('wad:home'))

class RegisterView(View):
    def get(self, request):
        user_form = UserForm()
        profile_form = UserProfileForm()
        return render(request, 'project/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': False})

    def post(self, request):
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
            registered = False
        return render(request, 'project/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


class MyRecipesView(View):
    def get(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        user_recipes = Recipe.objects.filter(user=user_profile)
        return render(request, 'project/MyRecipes.html', {'user_recipes': user_recipes})

@login_required
def rate_recipe(request):
    rating = request.POST.get('rating')
    recipe_id = request.POST.get('recipeID')

    if rating is not None and recipe_id is not None:
        recipe = get_object_or_404(Recipe, id=recipe_id)
        user_profile = request.user.userprofile

        if recipe.user == user_profile:
            message = message = f"You cannot rate your own recipe. Head over to the <a href='{reverse('wad:home')}'>homepage</a> or the <a href='{reverse('wad:cuisine')}'>cuisine page</a> and leave some feedback on other recipes."

            return HttpResponse(message)

        if starRating.objects.filter(userID=user_profile, recipeID=recipe).exists():
            cuisine_name = recipe.cuisine
            homepage_url = reverse('wad:home')
            cuisine_url = reverse('wad:' + cuisine_name.lower())
            message = f'You have already rated this recipe. Head back to the <a href="{homepage_url}">homepage</a> or the <a href="{cuisine_url}">{cuisine_name}</a> page to view and rate more recipes.'
            return HttpResponse(message)
        
        star_rating = starRating.objects.create(userID=user_profile, recipeID=recipe, rating=rating)
        avg_rating = recipe.starrating_set.aggregate(avg_rating=Avg('rating'))['avg_rating'] or 0
        return render(request, 'project/ViewRecipe.html', {'recipe': recipe, 'avg_rating': avg_rating})
    else:
        return JsonResponse({'error': 'Rating or Recipe ID missing'}, status=400)


class RecipeDeleteView(DeleteView):
    model = Recipe
    success_url = reverse_lazy('wad:myrecipes')