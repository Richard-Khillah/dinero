# Category.py
# class Category(Enum) is used to assing a category to a restaurant
# item. Variables can be assigned in the following ways:
#   1. catetory1 = Category.LUNCH           Traditional Hard Code idea
#   2. category2 = Category('lunch')    Assign based on value
#   3. category3 = Category['LUNCH']      Assign based on name (key)
#
# Note: catetory1 == category2 == category3, as one might expect, thus
# calling print() on either category (1-3) created above, yeilds the same
# output for each, namely: Category.LUNCH
#
# Category(Enum) have enherited properties `.name` and `.value`
# print(category1.name) prints `LUNCH`
# print(category1.vlaue) prints `lunch`

from enum import Enum
class Category(Enum):
    APPETIZER = 'appetizer'
    SNACK = 'snack'
    DESSERT = 'dessert'
    BREAKFAST = 'breakfast'
    LUNCH = 'lunch'
    DINNER = 'dinner'
    BEVERAGE = 'beverage'
    

NUM_TEST_ITEMS = 15
