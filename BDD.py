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

class Starring:
        starring_Encanto = ["Stephanie Beatriz", "Maria Cecilia Botero", "John Leguizamo", "Mauro Castillo"]
        starring_Titanic = ["Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates", "Frances Fisher"]
        starring_Turning_Red = ["Rosalie Chiang", "Sandra Oh", "Ava Morse", "Hyein Park", "Orion Lee"]
        starring_Avatar = ["Sam Worthington", "Zoe Saldana", "Stephen Lang", "Michelle Rodriguez", "Sigourney Weaver" ]
        starring_Wolf_of_Wall_Street = ["Leonardo DiCaprio", "Jonah Hill", "Margot Robbie", "Matthew McConaughey", "Kyle Chandler"]


FILMS = [
        {'name':'Encanto',
        'id' : 1,
        'Type': Type.Animated,
        'url':'https://en.wikipedia.org/wiki/Encanto_(film)',
        'year': '2021',
        'starring': Starring.starring_Encanto
        },
        {'name':'Titanic',
        'id' : 2,
        'Type': Type.Romantic,
        'url':'https://en.wikipedia.org/wiki/Titanic_(1997_film)',
        'year': '1997',
        'starring': Starring.starring_Titanic
        },
        {'name':'Turning red',
        'id' : 3,
        'Type': Type.Animated,
        'url':'https://en.wikipedia.org/wiki/Turning_Red',
        'year': '2022',
        'starring': Starring.starring_Turning_Red
        },
        {'name':'Avatar',
        'id' : 4,
        'Type': Type.Science_Fiction,
        'url':'https://en.wikipedia.org/wiki/Avatar_(2009_film)',
        'year': '2009',
        'starring': Starring.starring_Avatar
        },
        {'name':'Wolf of Wall Street',
        'id' : 5,
        'Type': Type.Comedy,
        'url':'https://en.wikipedia.org/wiki/The_Wolf_of_Wall_Street_(2013_film)',
        'year': '2013',
        'starring': Starring.starring_Wolf_of_Wall_Street
        },
        ]
