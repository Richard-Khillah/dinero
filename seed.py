from app import db

import sys

from app.auth.models.User import User
from app.auth import constants as USER

from app.restaurant.models.Restaurant import Restaurant

from app.item.models.Item import Item

from app.bill.models.Bill import Bill

db.drop_all()
db.create_all()

# Users

users = []

admin = User(name='admin', username='admin', email='admin@admin.com', password='password')
admin.role = USER.ADMIN
users.append(admin);

owner1 = User(name='owner1', username='owner1', email='owner1@owner1.com', password='password')
owner1.role = USER.OWNER
users.append(owner1);

owner2 = User(name='owner2', username='owner2', email='owner2@owner2.com', password='password')
owner2.role = USER.OWNER
users.append(owner2);

manager = User(name='manager', username='manager', email='manager@manager.com', password='password')
manager.role = USER.MANAGER
users.append(manager);

server = User(name='server', username='server', email='server@server.com', password='password')
server.role = USER.SERVER
users.append(server);

customer1 = User(name='customer1', username='customer1', email='customer1@customer1.com', password='password')
users.append(customer1);

customer2 = User(name='customer2', username='customer2', email='customer2@customer2.com', password='password')
users.append(customer2);

try:
    print('adding users')
    for user in users:
        db.session.add(user)
    db.session.commit()
except:
    print("Unexpected error:", sys.exc_info()[0])
    db.session.rollback()


starbucks = Restaurant(owner=owner1, name='Starbucks', restaurant_number=1, address='1 starbucks lane')

mcdonalds = Restaurant(owner=owner2, name='mcdonalds', restaurant_number=1, address='1 mcdonalds lane')

restaurants = [starbucks, mcdonalds]

try:
    print('adding rest')
    for rest in restaurants:
        db.session.add(rest)
    db.session.commit()
except:
    print("Unexpected error:", sys.exc_info()[0])
    db.session.rollback()


coffee = Item(name='black', cost=1.50, description='black coffee', category='beverage')
coffee.restaurant_id = starbucks.id

items1 = [coffee]
items2 = []
items3 = []

for i in range(1,5):
    name = 'Item' + str(i)
    cost = 1.99 + i
    desc = name + ' desc'
    item = Item(name=name, cost=cost, description=desc, category='beverage')
    item.restaurant_id = starbucks.id
    items1.append(item)

for i in range(5,10):
    name = 'Item' + str(i)
    cost = 1.99 + i
    desc = name + ' desc'
    item = Item(name=name, cost=cost, description=desc, category='snack')
    item.restaurant_id = starbucks.id
    items2.append(item)

for i in range(10,15):
    name = 'Item' + str(i)
    cost = 1.99 + i
    desc = name + ' desc'
    item = Item(name=name, cost=cost, description=desc, category='dinner')
    item.restaurant_id = mcdonalds.id
    items3.append(item)

items = items1 + items2 + items3

try:
    print('adding items')
    for item in items:
        db.session.add(item)
    db.session.commit()
except:
    print("Unexpected error:", sys.exc_info()[0])
    db.session.rollback()


bill1 = Bill(customer1, paid=False, receipt_number='1', message='have a good day')
bill1.items = items1
bill1.restaurant_id = starbucks.id

bill2 = Bill(customer2, paid=False, receipt_number='1', message='stuff here')
bill2.items = items2
bill2.restaurant_id = starbucks.id

bill3 = Bill(customer2, paid=False, receipt_number='2', message='free tacos')
bill3.items = items3
bill3.restaurant_id= mcdonalds.id

bills = [bill1, bill2]

try:
    print('adding bills')
    for bill in bills:
        db.session.add(bill)
    db.session.commit()
except:
    print("Unexpected error:", sys.exc_info()[0])
    db.session.rollback()
    
