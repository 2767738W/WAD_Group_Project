import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','wad_group_project.settings')

import django
django.setup()
from wad.models import Recipe, UserProfile, starRating
from django.contrib.auth.models import User




def populate():
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
            'image':'spagbol.jpg'
        },
        {
            'name':'Cacio e Pepe',
            'user':'michaelwoods15',
            'cuisine':'Italian',
            'ingredients':'''
                200g bucatini or spaghetti
                25g butter
                2 tsp whole black peppercorns, ground, or 1 tsp freshly ground black pepper
                50g pecorino or parmesan, finely grated
            ''',
            'instructions':'''
                Cook the pasta for 2 mins less than pack instructions state, in salted boiling water. Meanwhile, melt the butter in a medium frying pan over a low heat, then add the ground black pepper and toast for a few minutes.
                Drain the pasta, keeping 200ml of the pasta water. Tip the pasta and 100ml of the pasta water into the pan with the butter and pepper. Toss briefly, then scatter over the parmesan evenly, but don’t stir – wait for the cheese to melt for 30 seconds, then once melted, toss everything well, and stir together. This prevents the cheese from clumping or going stringy and makes a smooth, shiny sauce. Add a splash more pasta water if you need to, to loosen the sauce and coat the pasta. Serve immediately with a good grating of black pepper.
            ''',
            'image':'caciopepe.jpg'
        },
        {
            'name':'Minestrone Soup',
            'user':'michaelwoods15',
            'cuisine':'Italian',
            'ingredients':'''
                3 tbsp olive oil, plus extra to serve
                1 onion, finely chopped
                1 celery stick, finely chopped
                1 carrot, peeled and finely chopped
                1 courgette, finely chopped
                70g diced smoked pancetta
                1 large garlic clove, crushed
                ½ tsp dried oregano
                1 x 400g can cannellini beans
                1 x 400g can chopped tomatoes
                2 tbsp tomato purée
                1.2 litre vegetable stock
                1 bay leaf
                70g small pasta
                100g greens - kale, chard or cavolo nero work well
                handful of basil
                finely grated parmesan, to serve
            ''',
            'instructions':'''
                Heat the oil in a large saucepan or casserole pot over a low-medium heat and gently fry the onion, celery, carrot, courgette and pancetta for 10 mins. Add the garlic and oregano, and cook for 1 min. Tip in the beans, chopped tomatoes, purée, stock and bay leaf. Season to taste. Bring to the simmer and cook for 30 mins.
                Add the pasta and greens, and cook for a further 10 mins. Ladle into bowls and scatter with the basil and some parmesan.
            ''',
            'image':'minestrone.jpg'
        },
        {
            'name':'Chicken Noodle Soup',
            'user':'michaelwoods15',
            'cuisine':'Chinese',
            'ingredients':'''
                1 tbsp honey
                3 tbsp dark soy
                1 red chilli, sliced
                1l chicken stock
                80g leftover roast chicken (optional)
                20g pickled pink ginger or normal ginger, peeled and finely sliced
                ½ Chinese cabbage, shredded
                300g pouch straight-to-wok thick noodles
                4 spring onions, sliced
            ''',
            'instructions':'''
                Drizzle the honey over the base of a large saucepan and bubble briefly to a caramel, then splash in the soy, bubble, add half the chilli and the chicken stock and simmer for 5 mins.
                Add the chicken, if using, and ginger, and simmer for another 5 mins. Stir in the cabbage and noodles and cook until just wilted and the noodles have heated through. Ladle into bowls and sprinkle over the remaining chilli and the spring onions.
            ''',
            'image':'noodlesoup.jpg'
        },
        {
            'name':'Chinese Chicken Curry',
            'user':'michaelwoods15',
            'cuisine':'Chinese',
            'ingredients':'''
                4 skinless chicken breasts, cut into chunks (or use thighs or drumsticks)
                2 tsp cornflour
                1 onion, diced
                2 tbsp rapeseed oil
                1 garlic clove, crushed
                2 tsp curry powder
                1 tsp turmeric
                ½ tsp ground ginger
                pinch sugar
                400ml chicken stock
                1 tsp soy sauce
                handful frozen peas
                rice to serve
            ''',
            'instructions':'''
                Toss the chicken pieces in the cornflour and season well. Set them aside.
                Fry the onion in half of the oil in a wok on a low to medium heat, until it softens – about 5-6 minutes – then add the garlic and cook for a minute. Stir in the spices and sugar and cook for another minute, then add the stock and soy sauce, bring to a simmer and cook for 20 minutes. Tip everything into a blender and blitz until smooth.
                Wipe out the pan and fry the chicken in the remaining oil until it is browned all over. Tip the sauce back into the pan and bring everything to a simmer, stir in the peas and cook for 5 minutes. Add a little water if you need to thin the sauce. Serve with rice.
            ''',
            'image':'chickencurry.jpg'
        },
        {
            'name':'Char Siu',
            'user':'michaelwoods15',
            'cuisine':'Chinese',
            'ingredients':'''
                700g rindless pork belly
                For the marinade
                4 fat garlic cloves, finely chopped
                thumb-sized piece ginger, peeled and finely chopped
                4 tbsp tomato ketchup
                4 tbsp hoisin sauce
                4 tbsp golden caster sugar
                2 tbsp dark soy sauce
                2 tbsp rice vinegar
                2 tbsp sunflower oil
                To serve
                Pickled carrot & mooli (see 'Goes well with')
                4-5 spring onion, thinly sliced on the diagonal
                6 tbsp wasabi mayonnaise (or 6 tbsp mayo mixed with 1 tsp wasabi paste)
            ''',
            'instructions':'''
                Put the pork in a roasting tin, tip over all the marinade ingredients and massage it in with your fingers (or use a spoon) to coat the pork. Cover and chill overnight.
                Heat oven to 160C/140C fan/gas 3. Cover the tin with foil and cook the pork for 31/2 hrs, basting every hour. Increase the oven temperature to 180C/160C/gas 4, remove the foil, baste the pork and continue to cook for 45 mins until it is beginning to caramelise around the edges.
                Remove the pork from the tin and set aside to rest for 20 mins. Meanwhile, spoon away any fat from the tin and transfer the sauce to a small pan. Slice the pork – it will fall apart as you cut into it – then return to the tin. Warm the sauce in the pan, then pour over the meat and toss everything together. Spoon into the hot buns with the Pickled carrot & mooli, spring onions and a dollop of wasabi mayonnaise.
            ''',
            'image':'charsiu.jpg'    
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