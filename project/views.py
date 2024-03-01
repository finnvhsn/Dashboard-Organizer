from flask import Flask, Blueprint, render_template
import yfinance as yf
import plotly.express as px 


views = Blueprint('views', __name__)

@views.route('/dashboard', methods=['GET', 'POST'])
def home():
    
    my_graph = fetch_stock_data()
    weather_url= weather()
    
    return render_template("test.html", my_graph=my_graph, weather_url=weather_url), 200

#Diese Funktion crawlt Finanz-daten aus dem Internet mit API "Yahoo-Finance" und generiert eine Grafik daraus
def fetch_stock_data():
    stock_data = yf.download("AMZN", period="30d", interval="1h")
    my_graph = px.line(stock_data, y="High")
    my_graph= my_graph.to_html()
    
    return my_graph

#Diese Funktion verwendet ein fertiges Widget in Iframe format und verändert den Standort basiert auf der user-id
def weather():    
    user_nr= 3
    weather_url = "https://de.euronews.com/embed/wetter/europa/deutschland/" #Hier den gewünschten URL verlinken und ggf. auch verändern
    if user_nr==1:
        weather_url += "frankfurt-am-main"
    elif user_nr==2:
        weather_url+= "stuttgart"
    else:
        weather_url+= "berlin" 
    return weather_url
