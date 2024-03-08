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
        },
        {
            'name':'Butter Chicken',
            'user':'michaelwoods15',
            'cuisine':'Indian',
            'ingredients':'''
                3 tbsp lemon juice
                2-3 tbsp kashmiri chili powder or paprika
                4 skinless chicken breasts or 8 thigh fillets
                3 tbsp melted butter or ghee
                200ml plain yogurt
                1 tbsp crushed garlic
                1 tbsp finely grated ginger
                2 tbsp ground coriander
                2 tbsp ground cumin
                2 tsp amchoor powder (dried mango powder)
                1 tbsp dried fenugreek leaves, crushed
                1 tbsp dried mint leaves
                1 tsp plain salt
                3 tbsp vegetable oil
                1 tsp cumin seeds
                4-8 hot green chillies, sliced
                90g butter or ghee
                2 medium onions, finely chopped
                4 green cardamom pods, cracked
                ½ tbsp crushed garlic
                ½ tbsp grated ginger
                1 tsp ground turmeric
                2 tsp dried fenugreek leaves, crushed
                500ml passata, diluted with 150ml water
                2 tsp garam masala
                100ml single cream
                large pinch of coriander leaves, to garnish
            ''',
            'instructions':'''
                Rub the lemon juice and chilli powder or paprika into the chicken with a pinch of salt, then chill for 1 hr. Mix all the marinade ingredients together in a bowl, taste for seasoning, then add the chilled chicken. Mix well and chill for another 2 hrs.
                Thread the marinated chicken pieces onto metal skewers, reserving any leftover marinade. Grill over a hot barbecue for 5 mins, turning occasionally and basting with the melted butter or ghee. Alternatively, cook under a hot grill for 8-10 mins, turning occasionally. Don't worry if the chicken is a little under cooked, as it will finish cooking in the sauce. Remove the skewers to a board.
                To make the sauce, heat 2 tbsp vegetable oil in a wok or large frying pan and drop in a few cumin seeds. When they start sizzling, tip in the rest of the seeds. Swirl the pan, reduce the heat and add the green chillies. Stir once or twice until the skins of the chillies have blistered, then add the butter or ghee. Turn the heat up to high and continue to cook until all the butter or ghee has melted. Tip in the onions and fry for 10 mins until the onions are light brown and soft. If you prefer a smooth sauce, tip the mixture into a blender and blitz until smooth. Alternatively, scrape into a bowl and set aside.
                Wipe the pan clean with kitchen paper and heat the remaining oil. Drop in the crushed cardamom pods. When they have swelled and lightened in colour, reduce the heat, add the garlic and ginger and fry for 30 seconds, stirring continuously until you can no longer smell raw garlic and ginger. Return the cooked onion mixture to the pan and mix well. Add the turmeric and half the fenugreek leaves. Season with salt. Taste and adjust the seasoning if needed – if you like, you can add some chilli powder. Pour in the diluted passata, mix well and bring to the boil. Reduce the heat to a simmer and cook, covered and stirring occasionally, for around 20 mins. Oil will eventually rise to the surface when the sauce is cooked.
                Remove the chicken pieces from the skewers and chop into bite-sized pieces. Add these to the sauce along with any resting juices. Tip about 125ml warm water into the bowl with the reserved marinade, swirl to loosen, then stir into the sauce. Bring the sauce to the boil and reduce the heat to a simmer. Sprinkle over with garam masala and continue to cook for 3-4 minutes, or until chicken is cooked through. If you like, add a splash of boiling water to loosen the sauce, then taste for seasoning. Pour in half the cream and mix well.
            ''',
            'image':'butterchicken.jpg'
        },
        {
            'name':'Spiced Paneer',
            'user':'michaelwoods15',
            'cuisine':'Indian',
            'ingredients':'''
                vegetable oil, for frying
                400g paneer, cut into bite-sized pieces
                1 tsp coriander seed
                knob of ginger, peeled and chopped
                1 medium onion, chopped
                4 large ripe tomatoes, chopped
                1½ tsp chilli powder
                1 tsp fenugreek seed
                1 tsp garam masala
                1 tbsp clear honey
                small handful of fresh coriander, chopped
                small knob of ginger, peeled and shredded into matchsticks
                1 small red and 1 small green pepper, seeded and finely chopped
                3 spring onions, finely shredded
            ''',
            'instructions':'''
                Heat 1cm oil in a large frying pan and fry the paneer in batches until golden brown – watch out as the oil spits. Scoop it on to kitchen paper.
                Heat 1 tbsp oil in a frying pan and gently fry the coriander seeds, ginger, chilli and onion for about 8- 10 minutes until golden. Tip in the tomatoes and cook for another 5 minutes until they start to soften. Add the other spices and honey, stir and simmer for a few minutes.
                Tip the paneer into the sauce and stir. Simmer for a few minutes, then add the chopped coriander and shredded ginger. Serve sprinkled with peppers and spring onions.
            ''',
            'image':'paneer.jpg'
        },
        {
            'name':'Saag Aloo',
            'user':'michaelwoods15',
            'cuisine':'Indian',
            'ingredients':'''
                2 tbsp sunflower oil
                1 onion, finely chopped
                2 garlic cloves, sliced
                1 tbsp chopped ginger
                500g potato, cut into 2cm (¾in) chunks
                1 large red chilli, halved, deseeded and finely sliced
                ½ tsp each black mustard seeds, cumin seeds, turmeric
                250g spinach leaves
            ''',
            'instructions':'''
                Heat 2 tbsp sunflower oil in a large pan, add 1 finely chopped onion, 2 sliced garlic cloves and 1 tbsp chopped ginger, and fry for about 3 mins.
                Stir in 500g potatoes, cut into 2cm chunks, 1 halved, deseeded and finely sliced red chilli, ½ tsp black mustard seeds, ½ tsp cumin seeds, ½ tsp turmeric and ½ tsp salt and continue cooking and stirring for 5 mins more.
                Add a splash of water, cover, and cook for 8-10 mins.
                Check the potatoes are ready by spearing with the point of a knife, and if they are, add 250g spinach leaves and let it wilt into the pan. Take off the heat and serve.
            ''',
            'image':'saagaloo.jpg'
        },
        {
            'name':'Thai Red Curry',
            'user':'michaelwoods15',
            'cuisine':'Thai',
            'ingredients':'''
                1tbsp vegetable oil
                1tbsp ginger & garlic paste
                red curry paste
                800ml coconut milk
                8 skinless, boneless chicken thighs, cut into large chunks
                4 lime leaves (ideally fresh)
                2tbsp fish sauce
                1tsp brown sugar
                Thai basil
                basil or coriander, plus extra to serve
                1 red chilli, sliced diagonally
                thumb-sized piece ginger, cut into matchsticks
                cooked jasmine rice, to serve
            ''',
            'instructions':'''
                Heat 1 tbsp vegetable oil in a large saucepan over a medium heat and fry 1 tbsp ginger and 1 tbsp garlic paste for 2 mins. Add 5-6 tbsp red curry paste, sizzle for a few secs, then pour in 800ml coconut milk.
                Bring to the boil, reduce to a simmer, stir a little and wait for the oil to rise to the surface.
                Add 8 skinless, boneless chicken thighs, cut into chunks, and lime leaves, and simmer for 12 mins or until the chicken is cooked through.
                Add 1 tbsp of the fish sauce and a pinch of brown sugar, then taste – if you like it a little saltier, add more fish sauce; if you like it sweeter, add a little more sugar.
                Bring to the boil, take off the heat and add ½ small pack Thai basil.
                Spoon the curry into four bowls and top with 1 red chilli, a thumb-sized piece of ginger and a few extra basil leaves. Serve with jasmine rice.
            ''',
            'image':'redcurry.jpg'
        },
        {
            'name':'Thai Green Curry',
            'user':'michaelwoods15',
            'cuisine':'Thai',
            'ingredients':'''
                225g new potatoes, cut into chunks
                100g green beans, trimmed and halved
                1 tbsp vegetable or sunflower oil
                1 garlic clove, chopped
                1 rounded tbsp or 4 tsp Thai green curry paste (you can't fit the tablespoon into some of the jars)
                400ml can coconut milk
                2 tsp Thai fish sauce
                1 tsp caster sugar
                450g boneless skinless chicken (breasts or thighs), cut into bite-size pieces
                2 lime leaves finely shredded, or 3 wide strips lime zest, plus extra to garnish
                good handful of basil leaves
                boiled rice, to serve
            ''',
            'instructions':'''
                Put 225g new potatoes, cut into chunks, in a pan of boiling water and cook for 5 minutes.
                Add 100g trimmed and halved green beans and cook for a further 3 minutes, by which time both should be just tender but not too soft. Drain and put to one side.
                In a wok or large frying pan, heat 1 tbsp vegetable or sunflower oil until very hot, then drop in 1 chopped garlic clove and cook until golden, this should take only a few seconds. Don’t let it go very dark or it will spoil the taste.
                Spoon in 1 rounded tbsp Thai green curry paste and stir it around for a few seconds to begin to cook the spices and release all the flavours.
                Next, pour in a 400ml can of coconut milk and let it come to a bubble.
                Stir in 2 tsp Thai fish sauce and 1 tsp caster sugar, then 450g bite-size chicken pieces. Turn the heat down to a simmer and cook, covered, for about 8 minutes until the chicken is cooked.
                Tip in the potatoes and beans and let them warm through in the hot coconut milk, then add 2 finely shredded lime leaves (or 3 wide strips lime zest).
                Add a good handful basil leaves, but only leave them briefly on the heat or they will quickly lose their brightness.
                Scatter with lime to garnish and serve immediately with boiled rice.
            ''',
            'image':'greencurry.jpg' 
        },
        {
            'name':'Pad Thai',
            'user':'michaelwoods15',
            'cuisine':'Thai',
            'ingredients':'''
                250g pack medium rice noodle
                2 tsp tamarind paste
                3 tbsp fish sauce
                2 tsp sugar
                1 garlic clove
                3 spring onions
                2 tbsp vegetable oil
                1 egg
                200g pack large cooked prawn
                75g beansprout
                handful salted peanut, chopped to serve
                lime wedges, to serve
            ''',
            'instructions':'''
                Tip the noodles into a large bowl and pour over a kettle of boiling water until they are covered. Leave to stand for 5-10 mins until the noodles are soft, then drain well. (You can do this part ahead of time – then just run the noodles under cold water until cool, and toss through a little oil to stop them from sticking.) Next, mix together the tamarind paste, fish sauce and sugar in a small bowl.
                Peel and finely chop the garlic. Trim the ends off the spring onions and cut into thin slices about 1cm long. Heat a wok or large frying pan over a high heat. When it’s really hot (a drop of water should sizzle straight away), pour in the oil and swirl around. Tip in garlic and spring onions. To stir-fry, take a spatula or tongs and toss the veg around the wok so they’re moving all the time. Cook for 30 secs, just until they begin to soften.
                Push the vegetables to the sides of the wok, then crack the egg into the centre. Keep stirring the egg for 30 secs until it begins to set and resembles a broken-up omelette.
                Add the prawns and beansprouts, followed by the noodles, then pour over the fish sauce mixture. Toss everything together and heat through. Spoon out onto plates. Serve with some chopped peanuts sprinkled over and wedges of lime.
            ''',
            'image':'padthai.jpg'
        }
    ]

    add_recipes(recipes)




def add_recipes(recipes):
    for recipe_data in recipes:
        user_profile = UserProfile.objects.get(user__username=recipe_data['user'])
        
        cuisine_key = recipe_data['cuisine'].lower()  # Convert cuisine to lowercase
        cuisine_display = dict(Recipe.CUISINE_CHOICES).get(cuisine_key)

        if not cuisine_display:
            print(f"Invalid cuisine: {recipe_data['cuisine']}")
            continue

        recipe, created = Recipe.objects.get_or_create(
            name=recipe_data['name'],
            user=user_profile,
            cuisine=cuisine_key,
            ingredients=recipe_data['ingredients'],
            instructions=recipe_data['instructions'],
            image=recipe_data['image'],
            slug=recipe_data['name'].lower().replace(' ', '-'),
        )

        if created:
            print(f"Recipe '{recipe.name}' created with cuisine '{cuisine_display}'.")
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