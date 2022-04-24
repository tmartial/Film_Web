# Website description "My Cinema"
Our website allows you to keep informations about the movies that you watch and to score them. 
You can add movies with many informations like the release year, the wikipedia website, a score, the actors...

# Installation
To be able to go on the website you have to install a virtual environment.
For this, you have to copy and paste the following command in you terminal :

# set the environment(mac)
<br> python3 -m venv .venv
<br> .venv/bin/pip install FLask
<br> FLASK_ENV=development ./.venv/bin/flask run

# set the environment(Windows)
<br> py -3 -m venv .venv
<br> pip install Flask
<br> set FLASK_ENV=development
<br> flask run

# address of our Web
http://127.0.0.1:5000

# general information 
We tried to add a delete function but there was a conflict with the POST request method of the function movies_profile in app.py. Therefore, we decided to 
delete it in order to be able to give some new score. We keep in mind that the delete function would be an improvement of the website in the future. 
