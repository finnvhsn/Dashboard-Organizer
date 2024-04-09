
from flask import Flask
import yfinance as yf
import requests
import plotly.express as px


def fetch_stock_data():
    '''
    Author: Rafael Guaraldo
    Summary: Uses "Yahoo! Finance API" to scrappe stock prices from the last 30 days, 
             with intervals of one hour each. The collected data are plotted with Plotly Express and returned via "finances" in .html format
    Date: Feb 26th 2024
    Source: https://pypi.org/project/yfinance/ & https://finance.yahoo.com/
    '''
    
    #Scrappe one month worth of AAPL Stocks with an interval of one hour
    stock_data = yf.download("AAPl", period="30d", interval="1h")
    
    #Plotify the collected data and customize the Labels
    finances = px.line(stock_data, y="High", labels={"High": "AAPL"})
    
    #Converts the plot to html
    finances= finances.to_html()
    
    #Returns scrapped and plotted data as html
    return finances


# def weather():
#     '''
#     Author: Rafael Guaraldo
#     Summary: Sets an URL provided by "Euronews Weather-Widget" 
#              and returns it as "weather_url" to be modified for each individual user in later function
#     Date: Feb 28th 2024
#     Source: https://de.euronews.com/widgets
#     '''
    
#     #Sets the weather URL
#     weather_url = "https://de.euronews.com/embed/wetter/europa/deutschland/"
    
#     #returns the URL as "weather_url"
#     return weather_url



def get_weather_data():
    '''
    Author: Rafael Guaraldo
    Summary: Uses the "OpenWeather API" to scrappe real-time weather data from the given coordinates,
             jsonifies the data and returns them as "weather"
    Date: April 7th 2024
    Source: "https://openweathermap.org/current"
    '''
    # Define the API Key
    API_KEY = '63af8e971f2dca416a9dc9b2f05200ea'
    latitude = 48.8566
    longitude = 2.3522

    # Define the API endpoint
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric'
    
    try:
        # Send GET request to the API
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:

            # Parse the JSON response
            weather = response.json()

            # Return the weather data
            return weather

        # Return Error and status code 
        else:
            return "Failed to fetch data. Status code: {}".format(response.status_code)

    # General expetion handeling for "catching" error
    except requests.exceptions.RequestException as e:
        return "Error: {}".format(e)
 

def fetch_space_news():
    '''
    Author: Rafael Guaraldo
    Summary: Uses the "Spaceflight News API" to scrappe
             real-time news related to space programs, jsonifies the articles and returns them as "articles"
    Date: Mar 4th 2024
    Source: https://api.spaceflightnewsapi.net/documentation
    '''

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
        
        # Return Error and status code 
        else:
            return "Failed to fetch data. Status code: {}".format(response.status_code)
        
    # General expetion handeling for "catching" error
    except requests.exceptions.RequestException as e:
        return "Error: {}".format(e)
    

def fetch_f1_results():
    '''
    Author: Rafael Guaraldo
    Summary: Uses the F1-API provided by "Ergast Developer API" to scrappe 
             historycal F1 Results, parces and filters the data and returns it 
    Date: Mar 5th 2024
    Source: http://ergast.com/mrd/methods/results/
    '''
    
    # Define the API endpoint
    api_url = "https://ergast.com/api/f1/2023/results.json?limit=1000"
    
    try:
        # Send GET request to the API
        response = requests.get(api_url)
        
        # Raise an exception for HTTP errors
        response.raise_for_status()
        data = response.json()

        f1_results = []
        if 'MRData' in data and 'RaceTable' in data['MRData'] and 'Races' in data['MRData']['RaceTable']:
            
            # Extract race data
            races = data['MRData']['RaceTable']['Races']
            for race in races:
                race_name = race['raceName']
                results_data = []
               
                if 'Results' in race and race['Results']:
                    # Extract only top 3 race results for each race
                    results = race['Results']
                    
                    for result in results[:3]:
                        position = result['position']
                        driver_name = result['Driver']['givenName'] + " " + result['Driver']['familyName']
                        constructor = result['Constructor']['name']
                        results_data.append({'Position': position, 'Driver': driver_name, 'Constructor': constructor})
                f1_results.append({'Race': race_name, 'Results': results_data})
        
        # Return a list containing dictonaries of F1 Race Results
        return f1_results
    
    # Exeption handling
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        
    # Exeption handling
    except Exception as e:
        print(f"An error occurred: {e}")
        
    # Return empty list if exception occurs
    return []