import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','wad_group_project.settings')

import django
django.setup()
from wad.models import Recipe, UserProfile, starRating
from django.contrib.auth.models import User




def populate():
    IMAGE_PATH = 'population_script_images/'
    add_user()
    
    recipes = [
        {
            'name': 'Spaghetti Bolognese',
            'user': 'michaelwoods15',
            'cuisine': 'Italian',
            'ingredients': '''
                1 tbsp olive oil
                4 rashers smoked streaky bacon
                2 medium onions
                2 carrots
                2 celery sticks
                2 garlic cloves 
                -3 sprigs rosemary leaves
                500g beef mince
                2 x 400g tins plum tomatoes
                small pack basil leaves picked
                1 tsp dried oregano
                2 fresh bay leaves
                2 tbsp tomato purée
                1 beef stock cube
                1 red chilli
                400g spaghetti
            ''',
            'instructions': '''
                Add 4 finely chopped bacon rashers and fry for 10 mins until golden and crisp.
                Reduce the heat and add the 2 onions, 2 carrots, 2 celery sticks, 2 garlic cloves and the leaves from 2-3 sprigs rosemary, all finely chopped, then fry for 10 mins. Stir the veg often until it softens.
                Increase the heat to medium-high, add 500g beef mince and cook stirring for 3-4 mins until the meat is browned all over.
                Add 2 tins plum tomatoes, the finely chopped leaves from ¾ small pack basil, 1 tsp dried oregano, 2 bay leaves, 2 tbsp tomato purée, 1 beef stock cube, 1 deseeded and finely chopped red chilli (if using), 125ml red wine and 6 halved cherry tomatoes. Stir with a wooden spoon, breaking up the plum tomatoes.
                Bring to the boil, reduce to a gentle simmer and cover with a lid. Cook for 1 hr 15 mins stirring occasionally, until you have a rich, thick sauce.
                When the bolognese is nearly finished, cook 400g spaghetti following the pack instructions.
            ''',
            'image': IMAGE_PATH + 'spagbol.jpg'
        }
    ]

    add_recipes(recipes)




def add_recipes(recipes):
    for recipe_data in recipes:
        user_profile = UserProfile.objects.get(user__username=recipe_data['user'])

        recipe, created = Recipe.objects.get_or_create(
            name=recipe_data['name'],
            user=user_profile,
            cuisine=recipe_data['cuisine'],
            ingredients=recipe_data['ingredients'],
            instructions=recipe_data['instructions'],
            image=recipe_data['image'],
            slug=recipe_data['name'].lower().replace(' ', '-'),
        )

        if created:
            print(f"Recipe '{recipe.name}' created.")
        else:
            print(f"Recipe '{recipe.name}' already exists.")
    

def add_user():
    username = 'michaelwoods15'
    email = '2763066w@student.gla.ac.uk'
    password = 'password123'

    user, created = User.objects.get_or_create(
        username=username,
        email=email,
        defaults={'password': password}
    )

    if created:
        user_profile, _ = UserProfile.objects.get_or_create(
            user=user,
            forename='Michael',
            surname='Woods',
            dateOfBirth='2004-05-18',
            email=user.email,
        )
        print(f"User {username} created successfully.")
    else:
        print(f"User {username} already exists.")
    

if __name__ == '__main__':
    print("Starting  population script...")
    populate()