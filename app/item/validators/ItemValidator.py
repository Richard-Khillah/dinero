from wtforms import Form, StringField, IntegerField, FloatField, validators

#from app.item.constants import Category

class ItemValidator(Form):
    restaurant_id = IntegerField('Restaurant id', [
        validators.DataRequired(),
        validators.NumberRange(min=1, message='Restaurant id must be greater than 0.')
    ])

    name = StringField('Name', [
        validators.Length(min=2, max=50, message='Name must be between 2 and 50 characters.'),
        validators.DataRequired()
    ])

    cost = FloatField('Cost', [
        validators.DataRequired(),
        validators.NumberRange(min=1, message='Item cost must be greater than 0.')
    ])

    #category = StringField('category', [
    #    validators.DataRequired(),
    #])


    """
    #description is an optional field
    description = StringField('Description', [
        validators.DataRequired(),
        validators.StringField()
    ])
    """
