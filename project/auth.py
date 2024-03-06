from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user
from .models import add_user, check_user


auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(username) < 3:
            flash("Username must be at least 3 characters.")
        elif '@' not in email:
            flash("Email must include @")
        elif password1 is not None and len(password1) < 4:
            flash("password has to be at least 4 characters long.")
        elif password2 != password1:
            flash("Passwords must be the same.")
            
        else:

            add_user(username, email, password1)
            flash("User added successfully")
            return redirect(url_for('views.home'))        
        
    return render_template("register.html")


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = check_user(username, password)
        

        if user:
            
            login_user(user) 
            return redirect(url_for('views.home')) 
        else:
            error = 'Username or password is wrong.'
            return render_template("login.html", error=error)

    return render_template("login.html")