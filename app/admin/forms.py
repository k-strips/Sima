#importing Form
from flask_wtf import FlaskForm

#Importing form elements; textfield, passwordfield
from wtforms import StringField, PasswordField, SubmitField, TextField, SelectField

#Importing validators to validate Form
from wtforms.validators import DataRequired, Email

#Define the login form for site Admin
class AdminLogin(FlaskForm):
    admin_name = StringField("Admin Name", validators=[DataRequired()])
    admin_password = PasswordField('Admin Password', validators=[DataRequired()])
    submit = SubmitField("Login")

#define form for forgot_password page
class AdminForgot(FlaskForm):
    admin_name = StringField("Admin Name", validators=[DataRequired()])
    admin_email = StringField("Admin Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Reset Password")


#define the login form for lawyers
class AddLawyer(FlaskForm):
    lawyer_name = StringField("Attorney Name", validators=[DataRequired("PName of lawyer here")])
    lawyer_position = StringField("Position", [DataRequired("Lawyer's Position")])
    lawyer_phone = StringField("Contact Number", [DataRequired("lawyer's Contact")])
    lawyer_email = StringField("Email", [Email(message=("Not a valid email address")), DataRequired()])
    lawyer_bio = TextField()
    #lawyer_field = SelectField()
    lawyer_education = TextField()
    submit = SubmitField("Add Attorney")
