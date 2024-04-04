from flask import Flask, Blueprint, render_template, views
from project.endpoint import *


views = Blueprint('views', __name__)

@views.route("/landingpage")
def landingpage():
    return render_template("landingpage.html")

@views.route("/finn")
def page_user1():
    #Calls the returned value of fetch_stock_data function
    finances = fetch_stock_data() #Stockdata
    
    #Calls the returned value of weather function
    weather_url = weather()             
    
    #Modifies the URL to the user's location
    weather_url += "frankfurt-am-main" 
    
    #TODO Notizen fehlen
    return render_template("test.html", finances=finances, weather=weather_url)  


@views.route("/max")
def page_user2():
    #Calls the returned value of fetch_space_news function
    articles = fetch_space_news() #Space news
    
    #Calls the returned value of weather function
    weather_url = weather() 
    
    #Modifies the URL to the user's location
    weather_url += "berlin"
    
    #TODO Notizen fehlen
    return render_template("test.html", articles=articles, weather=weather_url) 


@views.route("/rafa")
def page_user3():
    #Calls the returned value of fetch_f1_results function
    f1_results = fetch_f1_results() 
    
    #Calls the returned value of weather function
    weather_url = weather()     
    
    #Modifies the URL to the user's location
    weather_url += "stuttgart"
    
    #TODO Notizen fehlen
    return render_template("test.html", f1_results=f1_results, weather=weather_url)
