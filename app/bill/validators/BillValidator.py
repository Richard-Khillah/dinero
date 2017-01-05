from wtforms import Form, StringField, BooleanField, DateTimeField, IntegerField, validators

class BillValidator(Form):
    paid = BooleanField('Paid')

    receipt_number = StringField('Receipt Number', [
        validators.DataRequired(),
        validators.Length(min=1, max=120, message='Receipt number must be between 1 and 120 characters.')
    ])

    customer_id = IntegerField('Customer Id', [
        validators.DataRequired(),
        validators.NumberRange(min=1, message='Customer id must be greater than 0.')
    ])

    message = StringField('Message', [
        validators.Length(max=120, message='Message must be less than 120 characters')
    ])

    created_at = DateTimeField('Created At')
