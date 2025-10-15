from flask import Blueprint, render_template, request, flash, redirect,  url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db 

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean= True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 4 charcters.', category= 'error')
        elif len(firstName) < 2:
            flash('firstName must be greater than 2 charcters.', category= 'error')
        elif password1 != password2 :
            flash('Passewords doesn\'t match .', category= 'error')
        elif len(password1) < 7 :
            flash('password must be at least 7 charcters.', category= 'error')
        else : 
            new_user = User(email = email, first_name= firstName, password = generate_password_hash(password1, method = 'sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created !', category= 'success')
            return redirect(url_for('views.home'))
            

    return render_template("sign_up.html")
