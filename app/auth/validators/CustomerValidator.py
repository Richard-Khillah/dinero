from wtforms import Form, StringField, PasswordField, validators


class CustomerValidator(Form):
    name = StringField('Full Name', [
        validators.Length(min=3,max=50,message='Name must be between 3 and 50 characters'),
        validators.DataRequired()
    ])

    username = StringField('Username', [
        validators.Length(min=3, max=20, message='Username must be between 3 and 20 characters.'),
        validators.DataRequired()
    ])

    email = StringField('Email Address', [
        validators.DataRequired(),
        validators.Email()
    ])

    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.Length(min=6, max=72, message='Password must be between 6 and 72 characters.')
    ])
