--------------------------------------------------Personal Dashboard-Organizer-------------------------------------------

This is a simple project for the Web Programming and Distributed Systems class. Our team's goal was to create a simple dashboard that would 
show useful information for each of our users. The Dashboard-Organizer V1 uses 4 different APIs to scrape real-time information 
and display it in a simple and logical way.

Programming languages:
    * Python: Python was chosen to program the backend and all the logic of this application. 

    * HTML and CSS: For the front-end, the main languages chosen were HTML, for displaying the scrapped data, and 
                    CSS, for styling the page elements.

Frameworks:
    * Flask: The whole application revolves around the Flask framework and its extensions, such as "login".
             For this project, Flask and its extensions were used to develop the web application and manage routing, view templating,
             user login and error handling. 

    * SQL Alchemy: This library was used to manage the tables responsible for creating and managing users and user data.
 

APIs:
    * Harvard Museum of Art API: This is a REST-style API that provides direct access to the data that powers the museum's website 
                                 and many other aspects of the museum.

    * Open Weather API: This API provides information about the current weather from anywhere in the world. It retrieves data from the OpenWeather
                        servers and provides a response in many different formats (HTML, JSON or XML).

    * Ergast F1 API: The Ergast Developer API is an experimental web service that provides a historical record of motor racing data. 
                     For this version, the program only retrieves and displays data from the 2024 F1 season. 

    * Spaceflight News 4.0 API: This API provides real time space related news from a variety of news sources.

This version of the Dashboard Organiser currently displays the same information to all of our users, but for future versions of this project 
we would like to implement personalised API parameters for each individual user. This means that different users should be able to see e.g.
a different collection of art from the Harvard Museum of Art, the weather from their current IP address location, and so on.



---------------------------------------How to Install and Run this Application-------------------------------------


1- Open the terminal of your choice (Ctrl + ` or Strg + Ö) and navigate to the /Dashboard-Organizer directory.

2- Once inside the directory, run "pip install -r requirements.txt" to install the necessary frameworks and libraries.

3- Once the requirements are installed, run the application by executing "main.py".
    -> Alternative 1: Run the command "python main.py" in the terminal
    -> Alternative 2: Open the main.py file and run it from there


--------------------------------------------How to Use this Application----------------------------------------------------


1. The application will open on the landing page, please login to continue

2. Use our default user to login:
    -Username: rafa
    -Password: abcdefg

3. Once logged in, you will be taken to that user's dashboard. Here you can see the data returned by each API.

4. If the user wants to see a different piece of art, simply refresh the page. In this version of the application 
   there are five selected artworks that can be displayed. 
   (Artworks are selected by their ID and sent as part of the GET request, no images have been preloaded and hardcoded)

DISCLAIMER: For presentation purposes, the routes are not protected by "login_required". This means that the user can easily access other 
            other users' dashboards without logging into their account first.     



------------------------------------------------------Credits-----------------------------------------------------------
Developer Team: 
- Finn Von Heesen
- Maximilian Schmidt
- Luis Muehmer
- Philipp Hiller
- Rafael Guaraldo Goulart

DHBW-Couse: WI IMBIT 2022 I-E

API sources:
- Harvard Museum of Art API: https://api.harvardartmuseums.org & https://github.com/harvardartmuseums/api-docs?tab=readme-ov-file
- Open Weather API: https://openweathermap.org/current
- Spaceflight News 4.0 API: https://api.spaceflightnewsapi.net/documentation & https://spaceflightnewsapi.net/
- Ergast F1 Api: http://ergast.com/mrd/
