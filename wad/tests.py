import os
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from wad.models import Recipe, UserProfile
from django.core.files.uploadedfile import SimpleUploadedFile


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.user_profile = UserProfile.objects.create(user=self.user)
        self.recipe = Recipe.objects.create(name='Test Recipe', cuisine='italian', user=self.user_profile, ingredients='',
                                            instructions='', image='fakeimage.jpg')

    def test_home_view(self):
        response = self.client.get(reverse('wad:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project/home.html')

    def test_cuisine_view(self):
        response = self.client.get(reverse('wad:cuisine'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project/Cuisine.html')

    def test_italian_view(self):
        response = self.client.get(reverse('wad:italian'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project/italian.html')

    def test_chinese_view(self):
        response = self.client.get(reverse('wad:chinese'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project/chinese.html')

    def test_thai_view(self):
        response = self.client.get(reverse('wad:thai'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project/thai.html')

    def test_indian_view(self):
        response = self.client.get(reverse('wad:indian'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project/indian.html')

    def test_view_recipe_view(self):
        response = self.client.get(reverse('wad:view_recipe', kwargs={'cuisine_name': 'italian', 'recipe_name_slug': self.recipe.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project/ViewRecipe.html')

    def test_user_login_view(self):
        response = self.client.get(reverse('wad:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project/login.html')

    def test_user_logout_view(self):
        response = self.client.get(reverse('wad:logout'))
        self.assertEqual(response.status_code, 302)  # Should redirect after logout

    def test_register_view(self):
        response = self.client.get(reverse('wad:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project/register.html')

    def test_my_recipes_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('wad:myrecipes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project/MyRecipes.html')

    def test_add_recipe_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('wad:addrecipe'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project/AddRecipe.html')
        
        image_filename = 'charsiu.jpg'
        image_path_source = os.path.join('../popscriptimages', image_filename)
        
        data = {
            'name': 'Test Recipe',
            'cuisine': 'italian',
            'ingredients': 'Test ingredient 1, Test ingredient 2',
            'instructions': 'Test instructions',
            'image': image_path_source,  
        }
        response = self.client.post(reverse('wad:addrecipe'), data, format='multipart')
        self.assertTrue(Recipe.objects.filter(name='Test Recipe').exists())
        created_recipe = Recipe.objects.get(name='Test Recipe')
        self.assertEqual(created_recipe.user, self.user.userprofile)


    def test_view_recipe_view(self):
        # Create a test recipe
        recipe = Recipe.objects.create(name='Spaghetti Bolognese', cuisine='Italian')

        response = self.client.get(reverse('wad:view_recipe', kwargs={'cuisine_name': 'italian', 'recipe_name_slug': recipe.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project/ViewRecipe.html')
