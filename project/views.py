from flask import Flask, Blueprint, render_template, views
from project.endpoint import *


views = Blueprint('views', __name__)

@views.route("/")
def landingpage():
    return render_template("landingpage.html")

@views.route("/all")
def page_user4():

    #Calls the returned value of fetch_random_painting function
    image = fetch_random_painting()

    # Calls the get_weather_data function to fetch weather data
    weather_data = get_weather_data()
    
    #Calls the returned value of fetch_space_news function
    articles = fetch_space_news()

    #Calls the returned value of fetch_f1_results function
    f1_results = fetch_f1_results() 
    
    return render_template("test.html", image=image, weather_data=weather_data, articles=articles, f1_results=f1_results)  


@views.route("/finn")
def page_user1():  
    #Calls the returned value of fetch_random_painting function
    image = fetch_random_painting()

    # Calls the get_weather_data function to fetch weather data
    weather_data = get_weather_data()
    
    #Calls the returned value of fetch_space_news function
    articles = fetch_space_news()

    #Calls the returned value of fetch_f1_results function
    f1_results = fetch_f1_results() 
    
    return render_template("test.html", image=image, weather_data=weather_data, articles=articles, f1_results=f1_results)  


@views.route("/max")
def page_user2():   
    #Calls the returned value of fetch_random_painting function
    image = fetch_random_painting()

    # Calls the get_weather_data function to fetch weather data
    weather_data = get_weather_data()
    
    #Calls the returned value of fetch_space_news function
    articles = fetch_space_news()

    #Calls the returned value of fetch_f1_results function
    f1_results = fetch_f1_results() 
    
    return render_template("test.html", image=image, weather_data=weather_data, articles=articles, f1_results=f1_results)  


@views.route("/rafa")
def page_user3(): 
    #Calls the returned value of fetch_random_painting function
    image = fetch_random_painting()

    # Calls the get_weather_data function to fetch weather data
    weather_data = get_weather_data()
    
    #Calls the returned value of fetch_space_news function
    articles = fetch_space_news()

    #Calls the returned value of fetch_f1_results function
    f1_results = fetch_f1_results() 
    
    return render_template("test.html", image=image, weather_data=weather_data, articles=articles, f1_results=f1_results)  


@views.route("/notes")
def notes():
    return render_template("notes.html")

