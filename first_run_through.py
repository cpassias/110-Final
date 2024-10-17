# Author: Cailey O'Connell, Cassie Passias
# Email: caileyoconne@umass.edu, cpassias@umass.edu
# Spire ID: 34689215, 34317403


# Step 1: import recipes 
recipes = [
        ('Macaroni & Cheese', ['milk', 'noodles', 'cheese']),
        ('Cheese Sticks', ['cheese', 'dough']),
        ('Cheese Bread', ['cheese', 'dough']),
        ('Baked Bread Sticks', ['bread']),
        ('Cheese Quesadillas', ['tortilla', 'cheese']),
        ('Chicken & Cheese Quesadillas', ['chicken', 'cheese', 'tortilla']),
        ('Meat & Cheese Quesadillas', ['meat', 'cheese', 'tortilla']),
        ('Ham & Cheese Sandwich', ['ham', 'cheese', 'bread']),
        ('Bacon & Cheese Sandwich', ['bacon', 'cheese', 'bread']),
        ('BLT Sandwich', ['bacon', 'tomatoes', 'bread', 'lettuce']),
        ('Fish Sandwich', ['fish', 'bread']),
        ('Turkey Sandwich', ['turkey', 'bread']),
        ('Turkey Sandwich w/Cheese', ['turkey', 'bread', 'cheese']),
        ('Sausage & Egg Muffin', ['sausage', 'eggs', 'muffins']),
        ('Scrambled Eggs', ['eggs']),
        ('Cheesy Scrambled Eggs', ['eggs', 'cheese']),
        ('Sunny Side Eggs', ['eggs']),
        ('Omelette', ['eggs']),
        ('Hot Dogs', ['buns', 'hotdog']),
        ('Chili Cheese Dogs', ['buns', 'hotdog', 'chili', 'cheese']),
        ('Tacos', ['meat', 'shell']),
        ('Tacos w/Chicken', ['chicken', 'shell']),
        ('Taco Salad', ['meat', 'chips', 'lettuce']),
        ('Grilled Chicken Salad', ['lettuce', 'chicken']),
        ('Grilled Chicken Avocado Salad', ['lettuce', 'chicken', 'avocado']),
        ('Grilled Cheese', ['cheese', 'bread']),
        ('French Toast', ['bread', 'eggs']),
        ('Burger', ['meat', 'buns']),
        ('Cheese Burger', ['meat', 'buns', 'cheese']),
        ('Pasta', ['noodles', 'sauce']),
        ('Pasta w/Meat', ['noodles', 'sauce', 'meat']),
        ('Spaghetti', ['noodles', 'sauce']),
        ('Alfredo', ['noodles', 'sauce']),
        ('Chicken Alfredo', ['noodles', 'sauce', 'chicken']),
        ('Shrimp Scampi Linguine', ['shrimp', 'sauce', 'noodles']),
        ('Chicken & Rice Combination', ['chicken', 'rice']),
        ('Ice Cream Shake Drink', ['ice cream', 'milk']),
        ('Baked potato', ['potatoes']),
        ('French Fries', ['potatoes']),
        ('Cheesy Baked potato', ['potatoes', 'cheese']),
        ('Chili', ['meat', 'tomatoes']),
        ('Chili Cheese French Fries', ['meat', 'tomatoes', 'potatoes', 'cheese']),
        ('Chili w/Beans', ['meat', 'tomatoes', 'beans']),
        ('Pizza', ['dough', 'sauce', 'cheese']),
        ('Pepperoni Pizza', ['dough', 'sauce', 'cheese', 'pepperoni']),
        ('Pizza w/Meat', ['dough', 'sauce', 'cheese', 'meat']),
        ('Pizza w/Chicken', ['dough', 'sauce', 'cheese', 'chicken']),
        ('Nachos w/Meat', ['chips', 'meat', 'salsa']),
        ('Nachos w/Chicken', ['chips', 'chicken', 'salsa']),
        ('Nachos w/Cheese', ['chips', 'meat', 'salsa', 'cheese']),
        ('Ice Cream Sandwiches', ['ice cream', 'crackers']),
        ('Smore Sandwiches', ['chocolate', 'crackers', 'marshmallows']),
        ('Fruit Salad', ['apple', 'banana', 'orange', 'grapes']),
        ('Fruit Smoothie', ['banana', 'strawberries', 'yogurt']),
        ('Caesar Salad', ['lettuce', 'croutons', 'parmesan', 'dressing']),
        ('Caprese Salad', ['tomatoes', 'mozzarella', 'basil', 'olive oil']),
        ('Grilled Shrimp', ['shrimp', 'garlic', 'lemon', 'butter']),
        ('Margarita Pizza', ['dough', 'tomatoes', 'mozzarella', 'basil', 'olive oil']),
        ('Vegetable Stir-Fry', ['broccoli', 'carrots', 'bell pepper', 'zucchini', 'soy sauce']),
        ('Spicy Tofu Curry', ['tofu', 'coconut milk', 'curry paste', 'bell pepper', 'onion']),
        ('Homemade Lasagna', ['lasagna noodles', 'ground beef', 'ricotta cheese', 'mozzarella cheese', 'tomato sauce']),
        ('Sushi Rolls', ['sushi rice', 'nori seaweed', 'fish', 'avocado', 'cucumber', 'soy sauce']),
        ('Spinach and Feta Stuffed Chicken', ['chicken breast', 'spinach', 'feta cheese', 'garlic', 'lemon']),
        ('Mango Salsa', ['mango', 'red onion', 'cilantro', 'lime juice']),
        ('Avocado Toast', ['avocado', 'bread', 'salt', 'pepper', 'red pepper flakes']),
        ('Chocolate Chip Cookies', ['flour', 'butter', 'sugar', 'chocolate chips', 'baking soda']),
        ('Fruit Smoothie Bowl', ['yogurt', 'banana', 'strawberries', 'granola', 'honey']),
        ('Pancakes', ['flour', 'milk', 'eggs', 'baking powder', 'syrup']),
        ('Greek Salad', ['cucumber', 'tomato', 'red onion', 'kalamata olives', 'feta cheese']),
        ('Hawaiian Pizza', ['dough', 'tomato sauce', 'ham', 'pineapple', 'mozzarella cheese']),
        ('Crispy Chicken Tenders', ['chicken tenders', 'flour', 'eggs', 'bread crumbs', 'spices']),
        ('Garlic Butter Shrimp', ['shrimp', 'butter', 'garlic', 'lemon juice', 'parsley']),
        ('Caprese Pasta Salad', ['pasta', 'tomatoes', 'mozzarella cheese', 'basil', 'balsamic dressing']),
        ('Veggie Burger', ['veggie patty', 'buns', 'lettuce', 'tomato', 'onion', 'mayonnaise']),
        ('Lemonade', ['lemons', 'sugar', 'water']),
        ('Cucumber Dill Salad', ['cucumbers', 'dill', 'onion', 'sour cream']),
        ('Tofu Scramble', ['tofu', 'bell pepper', 'onion', 'turmeric', 'spinach']),
        ('Cauliflower Rice', ['cauliflower', 'olive oil', 'garlic', 'spices']),
        ('Pulled Pork Sandwich', ['pork shoulder', 'buns', 'barbecue sauce', 'coleslaw']),
        ('Shrimp and Grits', ['shrimp', 'grits', 'bacon', 'cheese', 'green onions']),
        ('Ratatouille', ['eggplant', 'zucchini', 'tomatoes', 'bell pepper', 'garlic']),
        ('Stuffed Bell Peppers', ['bell peppers', 'ground beef', 'rice', 'tomato sauce', 'onion']),
        ('Garlic Knots', ['pizza dough', 'butter', 'garlic', 'parsley']),
        ('Peanut Butter and Jelly Sandwich', ['bread', 'peanut butter', 'jelly']),
        ('Scrambled Tofu', ['tofu', 'turmeric', 'black salt', 'pepper']),
        ('Vegetable Omelette', ['eggs', 'bell pepper', 'onion', 'mushrooms', 'cheese']),
        ('Pasta with Garlic and Olive Oil', ['spaghetti', 'garlic', 'olive oil', 'red pepper flakes']),
        ('Cereal with Milk', ['cereal', 'milk']),
        ('Fried Rice', ['cooked rice', 'vegetables', 'soy sauce', 'eggs']),
        ('Tomato Soup', ['tomatoes', 'onion', 'garlic', 'vegetable broth', 'cream']),
        ('Mashed Potatoes', ['potatoes', 'butter', 'milk']),
        ('Classic BLT Sandwich', ['bread', 'bacon', 'lettuce', 'tomato']),
        ('Oatmeal', ['oats', 'water', 'milk', 'sugar', 'cinnamon']),
        ('Chicken Noodle Soup', ['chicken broth', 'chicken', 'noodles', 'carrots', 'celery']),
        ('Greek Salad', ['cucumber', 'tomato', 'red onion', 'kalamata olives', 'feta cheese']),
    ]


# Step 2: ask user for ingredients and put them into a list
ingredients = []

num_of_ingredients = int(input("How many ingredients do you have? "))

for _ in range(num_of_ingredients):
    ingredient = input("Enter an ingredient: ")
    ingredients.append(ingredient)


# Step 3: eliminate recipes that user does not have all the ingredients for
def eliminate_recipes(recipes, ingredients):
    valid_recipes = [ ]
    for recipe_name, recipe_ingredients in recipes:
        for item in recipe_ingredients:
            if item not in ingredients:
                break
        else:
            valid_recipes.append(recipe_name)
    return valid_recipes

print("Your ingredients:")
print(ingredients)


# Step 4: match ingredients inputted with ingredients in recipes
match_recipes = eliminate_recipes(recipes, ingredients)

if match_recipes:
    print("You can make the following recipes:")
    for recipe in match_recipes:
        print(f"- {recipe}")
else:
    print("Sorry, you don't have enough ingredients for a recipe.")


# Older Code
'''for ingredients in num_of_ingredients:
    if ingredients in recipes:'''


'''def match_ingred():
    string = list(c)
    n = 0
    match_score = 0
    for ingredient in string:
        if ingredient in recipe:
            match_score += 1
            n += 1
        else:
           n += 1
    return match_score

print(match_ingred())'''


'''


# import data sort
# have user input ingredients

def enough_ingredients(c):
    c = list(c)
    if len(c) >= 3:
        match_ingred
    else:
        return ("You may have to buy more ingredients")
        

def match_ingred():
    string = list(c)
    n = 0
    match_score = 0
    for ingredient in string:
        if ingredient in recipe:
            match_score += 1
            n += 1
        else:
           n += 1
    return match_score

print(match_ingred())
print(enough_ingredients(c))



n = input("Enter ingredient: ")
match_score = 0

ingredients = []


c = input("Enter string of ingredients: ")
str = str(c)
n = 0
match_score = 0
recipe = ('bananas', 'milk', 'sugar', 'flour', 'eggs', 'cinnamon', 'baking powder', 'baking soda', 'salt')

def match_ingred(str):
    if str[n] in recipe:
        match_score += 1
        n += 1
    else:
        n += 1
    return()

print(match_score)
#if str[0] isin recipe, then check str[1]

# match up number of ingredients in fridge with those in a recipe
# output top 3 recipes from most to least matching
'''