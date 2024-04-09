from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required, login_user, logout_user
from project.models import User
from . import db


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
        elif len(password1) < 4:
            flash("Password must be at least 4 characters long.")
        elif password2 != password1:
            flash("Passwords must match.")
        else:
            # Create a new user object
            new_user = User(username=username, email=email, password=password1)
            # Add the new user to the database
            db.session.add(new_user)
            db.session.commit()
            flash("User added successfully")
            return redirect(url_for('views.landingpage'))
    
    return render_template("register.html")


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Query the database for the user
        user = User.query.filter_by(username=username).first()
        
        if user and user.password == password:
            # If user exists and password matches, log the user in
            login_user(user) 
          
            if user.username == 'finn':
                return redirect(url_for('views.page_user1'))    
            elif user.username == 'max':
                return redirect(url_for('views.page_user2'))
            elif user.username == 'rafa':
                return redirect(url_for('views.page_user3'))
            elif user.username is None:
                flash("You must fill in a username")
            elif user.username == username:
                if user.password == password:
                    return redirect(url_for('views.landingpage'))
        else:
            flash("Username or password is wrong")
            return render_template("login.html")

    return render_template("login.html", user = current_user)


@auth.route('/logout')
#Should be implemented with more details
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))