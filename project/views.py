from flask import Flask, Blueprint, render_template
import yfinance as yf
#import sqlite3
import plotly.express as px 


views = Blueprint('views', __name__)


@views.route('/dashboard', methods=['GET', 'POST'])
def home():
    
    my_graph = fetch_stock_data()
    weather_url= weather()
    
    return render_template("test.html", my_graph=my_graph, weather_url=weather_url), 200




#Diese Funktion crawlt Finanz-daten aus dem Internet mit API "Yahoo-Finance" und generiert eine Grafik daraus

#TODO NACHDEM EINE LOGIN FUNKTION,DIE DIE VARIABLE "ID" RETURNT GESCHRIEBEN WURDE, MUSS DIE FUNKTION ANHAND DER ID DEN URL VERÄNDERT

def fetch_stock_data():
    id=1    #-->ID ENTSPRICHT USER ID; DIE VON FUNKTION LOGIN GELIEFERT WIRD
    
    if   id==1:  
        stock_data = yf.download("AMZN", period="30d", interval="1h")
        
    elif id==2:
        stock_data = yf.download("GOOG", period="30d", interval="1h")
    
    else:
        stock_data = yf.download("AAPl", period="30d", interval="1h")
    my_graph = px.line(stock_data, y="High")
    my_graph= my_graph.to_html()
    return my_graph


#Diese Funktion verwendet ein fertiges Widget in Iframe format und verändert den Standort basiert auf der user-id

#TODO NACHDEM EINE LOGIN FUNKTION,DIE DIE VARIABLE "ID" RETURNT GESCHRIEBEN WURDE, MUSS DIE FUNKTION ANHAND DER ID DEN URL VERÄNDERT


def weather():    
    id=1 #-->ID ENTSPRICHT USER ID; DIE VON FUNKTION LOGIN GELIEFERT WIRD
    
    weather_url = "https://de.euronews.com/embed/wetter/europa/deutschland/" #Hier den gewünschten URL verlinken und ggf. auch verändern
    if id==1:  ##Vergleiche "username" und verändert die API zu seinem Standort  
        weather_url += "frankfurt-am-main"
    elif id==2:
        weather_url+= "stuttgart"
    else:
        weather_url+= "berlin" 
    return weather_url



# def weather():
#     # Connect to the SQLite database
#     conn = sqlite3.connect('myusers.db')
#     cursor = conn.cursor()

#     # Assume the table name is 'users' and 'id' is a column in that table
#     cursor.execute('SELECT id FROM users')
#     fetched_id = cursor.fetchone()  # Assuming you only need one id, otherwise use fetchall()

#     # Check if an id was fetched
#     if fetched_id:
#         fetched_id = fetched_id[0]  # Unpack the fetched id from the tuple
#     else:
#         # Default id if no id is found in the database
#         fetched_id = 1

#     # Construct the weather_url based on the fetched id
#     weather_url = "https://de.euronews.com/embed/wetter/europa/deutschland/"
#     if fetched_id == 1:
#         weather_url += "frankfurt-am-main"
#     elif fetched_id == 2:
#         weather_url += "stuttgart"
#     else:
#         weather_url += "berlin"

#     # Close cursor and connection
#     cursor.close()
#     conn.close()

#     return weather_url

