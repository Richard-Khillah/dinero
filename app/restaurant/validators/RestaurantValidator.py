from wtforms import Form, StringField, IntegerField, validators


class RestaurantValidator(Form):
    owner_id = IntegerField('Owner id', [
        validators.DataRequired(),
        validators.NumberRange(min=1, message='Owner id must be greater than 0')
    ])

    name = StringField('Name', [
        validators.Length(min=3,max=50,message='Name must be between 3 and 50 characters'),
        validators.DataRequired()
    ])

    address = StringField('Address', [
        validators.Length(min=3, max=120, message='Address must be between 3 and 120 characters.'),
        validators.DataRequired()
    ])

    restaurant_number = IntegerField('Restaurant Number', [
        validators.DataRequired(),
        validators.NumberRange(min=1, message='Restaurant Number must be greater than 0')
    ])
