"""
APPETIZER = 0
SNACK = 1
DESSERT = 2
BREAKFAST = 3
LUNCH = 4
DINNER = 5
BEVERAGE = 6

categories = {
    APPETIZER: 'appetizer',
    SNACK: 'snack',
    DESSERT: 'dessert',
    BREAKFAST: 'breakfast',
    LUNCH: 'lunch',
    DINNER: 'dinner',
    BEVERAGE: 'beverage'
}
"""

from enum import Enum
class Category(Enum):
    APPETIZER = 'appetizer'
    SNACK = 'snack'
    DESSERT = 'dessert'
    BREAKFAST = 'breakfast'
    LUNCH = 'lunch'
    DINNER = 'dinner'
    BEVERAGE = 'beverage'
