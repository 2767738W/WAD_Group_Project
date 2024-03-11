from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_POST
from django.db.models import Avg
from wad.forms import RecipeForm, UserForm, UserProfileForm
from wad.models import Recipe, starRating


#class HomeView(View):
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
    def get(self, request):
        form = RecipeForm()
        top_ten_recipes = Recipe.objects.annotate(avg_rating=Avg('starrating__rating')).order_by('-avg_rating')[:10]
        return render(request, 'project/AddRecipe.html', {'form': form, 'recipes': top_ten_recipes})

    def post(self, request):
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            return redirect(reverse('wad:view_recipe', kwargs={'recipe_name_slug': recipe.slug}))
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
    @login_required
    def get(self, request):
        user_recipes = Recipe.objects.filter(user=request.user)
        return render(request, 'project/MyRecipes.html', {'user_recipes': user_recipes})


@require_POST
def rate_recipe(request):
    try:
        recipe_id = request.POST['recipe_id']
        rating = int(request.POST['rating'])

        if rating < 1 or rating > 5:
            return JsonResponse({'error': 'Invalid rating value'}, status=400)

        recipe = get_object_or_404(Recipe, pk=recipe_id)
        starRating.objects.create(recipeID=recipe, rating=rating)

        return JsonResponse({'message': 'Rating submitted successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
