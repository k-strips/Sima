#Importing flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, redirect, url_for, g, current_app


#Importing the database from main app module
from app import db

#Importing module form
from app.admin.forms import AdminLogin, AddLawyer

#Importing admin from module models
from app.admin.models import Admin, Lawyer

#Defining admin blueprint with url prefix: app.url/admin
admin = Blueprint("admin", __name__, url_prefix="/admin")

#setting routes with methods
@admin.route("/")
@admin.route("/login", methods=['GET', 'POST'])
def login():
    form = AdminLogin()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(name=form.admin_name.data, password=form.admin_password.data).first_or_404()
        if admin.is_correct_password(form.admin.data):
            return redirect(url_for('admin.dashboard'))
    return render_template('admin/auth/login.html', form=form)


"""@admin.route("/forgot_password", methods=['GET', 'POST'])
def forgot():
    #
    form = AdminForgot()

    if form.validate_on_submit():
        try:
            admin = Admin.query.filter_by(name=form.admin_name.data).first()
            if admin.name == form.admin_name.data and admin.email == form.admin_email
        except ValueError:
            return render_template("404.html")
    return render_template("admin/auth/forgot.html", form=form, title="Forgot Password")
"""


@admin.route("/dashboard")
def dashboard():
    lawyers = Lawyer.query.all()
    return render_template("admin/pages/dashboard.html", lawyers=lawyers)


@admin.route("/add_attorney", methods=['GET', 'POST'])
def addAttorney():
    #import form to add lawyers from form
    form = AddLawyer()

    #checking if form is validated and submitted
    if form.validate_on_submit():
        lawyer = Lawyer(name=form.lawyer_name.data, position=form.lawyer_position, phone=form.lawyer_phone.data, email=form.lawyer_email.data)
        #lawyer.add_bio(form.lawyer_bio.data)
        #lawyer.add_education(form.lawyer_education.data)
        db.session.add(lawyer)
        db.session.commit()
        flash(f"{lawyer.name} added" ,"success")
    return render_template("admin/pages/manage_lawyers.html", form=form)


@admin.route("/delete_attorney/<int:id>", methods=["GET", "POST"])
def delete_attorney(id):
    attorney = Lawyer.query.get(id)
    db.session.delete(attorney)
    db.session.commit()
    flash('Lawyer successfully removed', 'success')
    return redirect(url_for('admin.dashboard'))
