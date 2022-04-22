import json
class Type:
        Action = "Action"
        Animated = "Animated"
        Comedy = "Comedy"
        Crime = "Crime"
        Documentary = "Documentary"
        Drama = "Drama"
        Fanstastic = "Fantastic"
        Horror = "Horror"
        Romantic = "Romantic"
        Science_Fiction = "Science Fiction"
        Thriller = "Thriller"



FILMS = [{'name':'Encanto',
        'id' : 1,
        'Type': Type.Animated,
        'url':'https://en.wikipedia.org/wiki/Encanto_(film)',
        'year': '2021',
        'starring': ["Stephanie Beatriz", "Maria Cecilia Botero", "John Leguizamo", "Mauro Castillo"],
        'film_length' : '1h49',
        'cover_url':'https://m.media-amazon.com/images/I/61mP-+-eH2L.jpg',
        'score': [3.8] # je le mets dans une liste pour pouvoir faire des moyennes de listes qd on append un score
        },
        {'name':'Titanic',
        'id' : 2,
        'Type': Type.Romantic,
        'url':'https://en.wikipedia.org/wiki/Titanic_(1997_film)',
        'year': '1997',
        'starring': ["Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates", "Frances Fisher"],
        'film_length' : '3h14',
        'cover_url':'https://filmxposure.files.wordpress.com/2015/08/titanic-cover.jpg',
        'score':[4.3]  #aussi c'est le résultat de allo ciné
        },
        {'name':'Turning red',
        'id' : 3,
        'Type': Type.Animated,
        'url':'https://en.wikipedia.org/wiki/Turning_Red',
        'year': '2022',
        'starring': ["Rosalie Chiang", "Sandra Oh", "Ava Morse", "Hyein Park", "Orion Lee"],
        'film_length' : '1h40',
        'cover_url':'https://mobile-img.lpcdn.ca/v2/924x/d38ad891cab2355483bf025e54322338.jpg',
        'score': [3.5]
        },
        {'name':'Avatar',
        'id' : 4,
        'Type': Type.Science_Fiction,
        'url':'https://en.wikipedia.org/wiki/Avatar_(2009_film)',
        'year': '2009',
        'starring': ["Sam Worthington", "Zoe Saldana", "Stephen Lang", "Michelle Rodriguez", "Sigourney Weaver" ],
        'film_length' : '2h42',
        'cover_url':'https://fr.web.img6.acsta.net/medias/nmedia/18/78/95/70/19485155.jpg',
        'score':[4.3]
        },
        {'name':'Wolf of Wall Street',
        'id' : 5,
        'Type': Type.Comedy,
        'url':'https://en.wikipedia.org/wiki/The_Wolf_of_Wall_Street_(2013_film)',
        'year': '2013',
        'starring': ["Leonardo DiCaprio", "Jonah Hill", "Margot Robbie", "Matthew McConaughey", "Kyle Chandler"],
        'film_length' : '3h',
        'cover_url':'https://images-na.ssl-images-amazon.com/images/I/914oHftat8L.jpg',
        'score':[4.2]
        }]

filename = "dict.json"
# Writing the list of dict objects to a file
with open(filename, mode='w') as f:
    json.dump(FILMS, f)
