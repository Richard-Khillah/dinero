
def addTestItems():
    from flask import jsonify

    from app.item.controller import dbs
    from app.item.models.Item import Item

    from app.item.constants import Category, NUM_TEST_ITEMS

    for i in range(1,NUM_TEST_ITEMS+1):
        restaurant_id= 1
        name = 'item'+str(i)
        cost = 10.99 + i
        description = 'Description for Item%d' % i
        if i % 7 == 1:
            category = Category.APPETIZER
        elif i % 7 == 2:
            category = Category.SNACK
        elif i % 7 == 3:
            category = Category.DESSERT
        elif i % 7 == 4:
            category = Category.BREAKFAST
        elif i % 7 == 5:
            category = Category.LUNCH
        elif i % 7 == 6:
            category = Category.DINNER
        elif i % 7 == 0:
            category = Category.BEVERAGE
        else:
            category = None
        try:
            item = Item(name, cost, description, category)
            dbs.add(item)
            dbs.commit()
            i += 1
        except:
            dbs.rollback()
            return jsonify({
                'status': 'error',
                'message': 'there was an running addTestItems().'
            })
    items = Item.query.all()
    for item in items:
        print(str(item))
    return jsonify({
        'status': 'success',
        'message': '%d items were added.' %i
    })
