# Website description "My Cinema"
Our website allow you to keep informations about the movies that you watch and to score them. 
You can add movies with many informations like the release year, the wikipedia website, a score, the actors...

# Installation
To be able to go on the website you have to install a virtual environment.
For this, you have to copy and paste the following command in you terminal :

# set the environment(mac)
$ python3 -m venv .venv
$ .venv/bin/pip install FLask
FLASK_ENV=development ./.venv/bin/flask
touch .gitignore
echo .venv > .gitignore

# set the environment(Windows)
py -3 -m venv .venv
pip install Flask
set FLASK_ENV=development
flask run
touch .gitignore
echo .venv > .gitignore

# address of our Web
http://127.0.0.1:5000
