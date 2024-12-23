# Author: Cailey O'Connell, Cassie Passias
# Email: caileyoconne@umass.edu, cpassias@umass.edu
# Spire ID: 34689215, 34317403

import os
os.system('cls' if os.name == 'nt' else 'clear')

# Step 1: import recipes 
from recipes import recipes
from websites import websites


# Step 2: ask user for ingredients and put them into a list
ingredients = []

while True:
    try:
        num_of_ingredients = int(input("How many ingredients do you have? "))
        print("\n")
        break  # Exit the loop if the input is valid
    except ValueError:
        print("\n")
        print("Invalid choice, please input an integer.")
        print("\n")


for _ in range(num_of_ingredients):
    ingredient = input("Enter an ingredient: ")
    ingredients.append(ingredient)
    print("\n")


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
print("\n")


# Step 4: match ingredients inputted with ingredients in recipes
match_recipes = eliminate_recipes(recipes, ingredients)

if match_recipes:
    print("You can make the following recipes:")
    i = 0
    for recipe in match_recipes:
        i += 1
        print(i, f"- {recipe}")
    invalid_choice = True
    while(invalid_choice):
        print("\n")
        choice = input("Which would you like to choose? ")
        print("\n")
        try:
            choice = (int)(choice)
        except:
            print("Invalid choice, choose a number listed.")
        else:
            if not (1 <= choice and choice <= i):
                print("Invalid choice, choose a number listed.")
            else:
                invalid_choice = False
                print("Take a look at the following recipe & enjoy!")
                print(websites[match_recipes[choice-1]],"\n")
else:
    print("Sorry, you don't have enough ingredients for a recipe.\n")
    print("Take a look at this site to explore some possible savory recipes:\nhttps://www.nytimes.com/article/easy-dinner-ideas.html\n")
    print("And don't forget your sweets!\nhttps://www.food.com/ideas/top-dessert-recipes-6930#c-791401\n")


# Scrapped
'''
# Step 5: ask to choose a recipe
def recipe_options():
    valid_recipes = []
    for recipe in match_recipes:
        valid_recipes.append(recipe)
    return valid_recipes
    options = input("What recipe would you like to make?")
    if options not in valid_recipes:
        print("Sorry, that is not a valid recipe.")
    else:
        if options in valid_recipes:
'''


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