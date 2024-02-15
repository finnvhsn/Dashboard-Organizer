from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/dashboard')
def home():
    return render_template("test.html")


