from flask import Flask, Blueprint, render_template
import yfinance as yf
import requests
#import sqlite3
import plotly.express as px

views = Blueprint('views', __name__)

# Das ist die "Basis" Version einer Route
@views.route('/dashboard', methods=['GET', 'POST'])
def home():
    
    my_graph = fetch_stock_data()
    weather_url= weather()
    articles = space_news()    
    return render_template("test.html", my_graph=my_graph, weather_url=weather_url, articles=articles), 200



#IGNORE THE FOLLOWING FUNCTIONS

###########################################################
# @views.route("/user1")
# def page_user1():
#     # Finanzen
#     # Wetter in Frankfurt
#     # Notizen
#     return None

# @views.route("/user2")
# def page_user2():
#     # Wetter in Berlin
#     # Space news
#     # Notizen
#     return None

# @views.route("/user3")
# def page_user2():
#     # Wetter in Stuttgart
#     # Rennergebnisse Formel 1
#     # Notizen
#     return None

#################################################################


#Diese Funktion crawlt Finanz-daten aus dem Internet mit API "Yahoo-Finance" und generiert eine Grafik daraus
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

# Bitte diese Funktion ignorieren

# def stocks_2():
#     # Download stock data for multiple stocks
#     stocks = ['AAPL', 'GOOGL', 'AMZN']
#     stock_data = yf.download(stocks, period="7d", interval="1h")

#     # Create a new plot
#     bokeh_plot = figure(x_axis_type="datetime", title="High Prices of Stocks")

#     # Create a ColumnDataSource for the stock data
#     source = ColumnDataSource(data=stock_data)

#     # Add high prices of each stock to the plot
#     for stock in stocks:
#         bokeh_plot.line(x='Datetime', y='High_' + stock, source=source, legend_label=stock, line_width=2)

#     # Add hover tool
#     hover = HoverTool(tooltips=[
#         ("Date", "@Datetime{%F}"),
#         ("Price", "@High{%F}")
#           ], 

#     formatters={"@Datetime": "datetime",
#                 "@High": "printf"})     
#     bokeh_plot.add_tools(hover)

#     # Customize the plot
#     bokeh_plot.xaxis.axis_label = 'Date'
#     bokeh_plot.yaxis.axis_label = 'Price in U$'
#     bokeh_plot.legend.location = "bottom_right"

#     # Convert plot to components
#     script, div = components(bokeh_plot)

#     return script, div


#Diese Funktion verwendet ein fertiges Widget in Iframe format und verändert den Standort basiert auf der user-id
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


# Diese Funktion verwendet die "Spaceflight News" API um Echtzeitdaten zu scrappen und stellt die 3 letzten Nachrichten zum Thema "Space" dar
def space_news():
    # Define the API endpoint
    url = "https://api.spaceflightnewsapi.net/v3/articles?_limit=3"

    try:
        # Send GET request to the API
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            articles = response.json()

            # Render the template with the articles data
            return articles
        else:
            return "Failed to fetch data. Status code: {}".format(response.status_code)

    except requests.exceptions.RequestException as e:
        return "Error: {}".format(e)



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