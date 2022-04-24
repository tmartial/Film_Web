# Website description "My Cinema"
Our website allow you to keep informations about the movies that you watch and to score them. 
You can add movies with many informations like the release year, the wikipedia website, a score, the actors...

# Installation
To be able to go on the website you have to install a virtual environment.
For this, you have to copy and paste the following command in you terminal :

# set the environment(mac)
<br> python3 -m venv .venv
<br> .venv/bin/pip install FLask
<br> FLASK_ENV=development ./.venv/bin/flask
<br> touch .gitignore
<br> echo .venv > .gitignore

# set the environment(Windows)
<br> py -3 -m venv .venv
<br> pip install Flask
<br> set FLASK_ENV=development
<br> flask run
<br> touch .gitignore
<br> echo .venv > .gitignore

# address of our Web
http://127.0.0.1:5000
