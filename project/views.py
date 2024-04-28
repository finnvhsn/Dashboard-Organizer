from datetime import datetime
from flask import Flask, Blueprint, jsonify, redirect, render_template, request, url_for, views
from flask_login import current_user, login_required
from project.endpoint import *
from project.models import Note
from . import db


views = Blueprint('views', __name__)

@views.route("/")
def landingpage():
    return render_template("landingpage.html")

@views.route("/finn")
def page_user1():  
    #Calls the returned value of fetch_random_painting function
    image, painting_id = fetch_random_painting()

    # Calls the get_weather_data function to fetch weather data
    weather_data = get_weather_data()
    
    #Calls the returned value of fetch_space_news function
    articles = fetch_space_news()

    #Calls the returned value of fetch_f1_results function
    f1_results = fetch_f1_results() 
    
    return render_template("test.html", image=image, painting_id=painting_id, weather_data=weather_data, articles=articles, f1_results=f1_results)  


@views.route("/max")
def page_user2():   
    #Calls the returned value of fetch_random_painting function
    image, painting_id = fetch_random_painting()

    # Calls the get_weather_data function to fetch weather data
    weather_data = get_weather_data()
    
    #Calls the returned value of fetch_space_news function
    articles = fetch_space_news()

    #Calls the returned value of fetch_f1_results function
    f1_results = fetch_f1_results() 
    
    return render_template("test.html", image=image, painting_id=painting_id, weather_data=weather_data, articles=articles, f1_results=f1_results)  


@views.route("/rafa")
def page_user3(): 
    #Calls the returned value of fetch_random_painting function
    image, painting_id = fetch_random_painting()

    # Calls the get_weather_data function to fetch weather data
    weather_data = get_weather_data()
    
    #Calls the returned value of fetch_space_news function
    articles = fetch_space_news()

    #Calls the returned value of fetch_f1_results function
    f1_results = fetch_f1_results() 
    
    return render_template("test.html", image=image, painting_id=painting_id, weather_data=weather_data, articles=articles, f1_results=f1_results)  


@views.route("/notes", methods=["GET", "POST"])
@login_required
def note():
    if request.method == 'POST': 
        note_text = request.form.get('note')
        print(f"Received note text: {note_text}")        
  
    return render_template("notes.html", user=current_user)

    
@views.route("/add_note", methods=["POST"])
@login_required
def add_note():

    if request.method == 'POST': 
        data = request.get_json()
        note_text = data.get('note')
        if note_text:
            new_note = Note(data=note_text, user_id=current_user.id, date=datetime.now())
            db.session.add(new_note)
            db.session.commit()
            return jsonify({'message': 'Note added successfully'}), 200
        else:
            return jsonify({'message': 'Note text is missing'}), 400

    user_notes = current_user.notes 
    return render_template("notes.html", user=current_user, notes=user_notes)
    

@views.route("/delete_note/<int:note_id>", methods=["DELETE"])
@login_required
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)

    if note.user_id == current_user.id:
        try:
            db.session.delete(note)
            db.session.commit()
            return jsonify({'message': 'Note deleted successfully'}), 200
        except Exception as e:
            return jsonify({'message': f'Failed to delete note: {str(e)}'}), 500
    else:
        return jsonify({'message': 'Unauthorized to delete this note'}), 403






######## The following functions and routes are for deleting values from each table in the database ########
    
    
def delete_all_notes():
    try:
    
        db.session.query(Note).delete()
        db.session.commit()
        print("All values from the Note table have been deleted.")
    except Exception as e:
        print(f"Error while deleting: {str(e)}")
        db.session.rollback() 


@views.route("/delete_all_notes", methods=["GET"])
def delete_all_notes_view():
    delete_all_notes()
    return "All notes have been deleted successfully."


def delete_all_users():
    try:
       
        db.session.query(User).delete()
        db.session.commit()
        print("All values from the User table have been deleted.")
    except Exception as e:
        print(f"Error while deleting: {str(e)}")
        db.session.rollback() 


@views.route("/delete_all_users", methods=["GET"])
def delete_all_users_view():
    delete_all_users()
    return "All users have been deleted successfully."