"""This program generates random bagel orders. I tried to pick flavors and ingredients that are actually available at bagel shops, but admittedly I'm out of touch and don't really know everything that's out there nowadays. Avocados, probably? The program also demands you get your bagel toasted, I don't care how hot and fresh it is."""

import random

#Here are your flavor/ingredient options
bagel = ("plain", "everything", "egg", "onion", "sesame", "poppy", "salt", "garlic", "whole wheat", "pumpernickel", "french toast", "cinnamon raisin")
schmear = ("plain cream cheese", "vegetable cream cheese", "butter", "peanut butter", "strawberry cream cheese", "garlic chive cream cheese")
toppings = ("lox", "onions", "red onions", "capers", "tomatoes", "grape jelly", "egg and cheese")

bagel_flavor = random.choice(bagel)

schmear_flavor = random.choice(schmear)

num_toppings = random.randint(-1, len(toppings))
#I think there's an issue with that -1, but I want to preserve the possibility of no non-schmear toppings at all
end_toppings = " "
for i in range(num_toppings):
    end_toppings += random.choice(toppings) + ", "
#also this for-loop allows for repeatedly choosing the same topping
#you could probably just change the topping tuple into a mutable list and pop the chosen topping off, since it's not like this program is built for more than a one-time order
#I kinda think it's funnier this way tho
#"plain bagel, toasted, with egg and cheese, egg and cheese, egg and cheese, a schmear of butter"

print(bagel_flavor + " bagel, toasted, with" + end_toppings + "a schmear of " + schmear_flavor)
