
from flask import Flask
import random
import requests


def fetch_random_painting():
    '''
    Author: Rafael Guaraldo
    Summary: Uses the official "Harvard Museum API" to scrappe art pieces from the museum's inventory.  
             To speed up the fetching, only a couple of paintings (selected by their ID) will be displayed
    Date: April 13th 2024
    Source: https://github.com/harvardartmuseums/api-docs & https://api-toolkit.herokuapp.com/
    '''
    # Define the API Key
    Painting_KEY = "b047612c-7da3-419b-96c6-2f38cff69d1b"
    # Define the base-Url
    BASE_URL = "https://api.harvardartmuseums.org"

    # Define the paintings to show
    painting_ids = ["232037","230721","231248", "4988", "304349"]
    painting_id = random.choice(painting_ids)

    try:
        # Define the API-Endpoint
        endpoint = f"{BASE_URL}/object/{painting_id}?apikey={Painting_KEY}"

        # Send GET request to the API
        response = requests.get(endpoint)
        data = response.json()

        # Check if the data contains images
        if 'images' in data and data['images']:
            image_url = data['images'][0]['baseimageurl']
            # Print image ID for debugging
            print (painting_id)
            # Return the URL of the image
            return image_url
        else:
            # Return error message if no images found
            return "Failed to fetch image. Status code: {}".format(response.status_code)
        
    # General expetion handeling for "catching" error
    except requests.exceptions.RequestException as e:
        return "Error: {}".format(e)


def get_weather_data():
    '''
    Author: Rafael Guaraldo
    Summary: Uses the "OpenWeather API" to scrappe real-time weather data from the defined coordinates,
             parse the data and returns them as the json-object "weather"
    Date: April 7th 2024
    Source: "https://openweathermap.org/current"
    '''
    # Define the API Key
    Weather_KEY = '63af8e971f2dca416a9dc9b2f05200ea'
    latitude = 48.7761648 #Coordinates to desired city
    longitude = 9.1730105 #Coordinates to desired city

    # Define the API endpoint
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={Weather_KEY}&units=metric'
    
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
    Date: Mar 4th 2024/ Updated to V4 on the 09th April 2024
    Source: https://api.spaceflightnewsapi.net/documentation
    '''

    # Define the API endpoint for V4
    url = "https://api.spaceflightnewsapi.net/v4/articles?_limit=3"
    try:
        # Send GET request to the APIS
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            
            # Parse the JSON response
            data = response.json()

            # In V4, the articles are under the "results" key in the response
            articles = data["results"]

            # Return the articles
            return articles
        
        # Return Error and status code 
        else:
            return "Failed to fetch data. Status code: {}".format(response.status_code)
        
    # General exception handling for "catching" error
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
    api_url = "https://ergast.com/api/f1/2024/results.json?limit=300"
    
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