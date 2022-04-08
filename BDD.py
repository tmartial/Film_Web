film_id = {"Encanto" : 1,
        "Titanic": 2,
        "Turning red": 3,
        "Avatar": 4 , 
        "Wolf of Wall Street": 5}
print("id of the film Encanto :", film_id["Encanto"])

film_type_list = [ "Action",
                "Animated",
                "Comedy",
                "Crime",
                "Documentary", 
                "Drama", 
                "Fantastic", 
                "Horror", 
                "Romantic", 
                "Science Fiction",
                "Thriller"]
print("List of type for the films", film_type_list)

film_type = {"Encanto": film_type_list[1],
        "Titanic": film_type_list[8],
        "Turning red": film_type_list[1],
        "Avatar": film_type_list[9],
        "Wolf of Wall Street": film_type_list[2]}
print("Type of the film Encanto :",film_type["Encanto"])

film_url = {"Encanto": "https://en.wikipedia.org/wiki/Encanto_(film)",
            "Titanic": "https://en.wikipedia.org/wiki/Titanic_(1997_film)", 
            "Turning red":"https://en.wikipedia.org/wiki/Turning_Red",
            "Avatar":"https://en.wikipedia.org/wiki/Avatar_(2009_film)", 
            "Wolf of Wall Street": "https://en.wikipedia.org/wiki/The_Wolf_of_Wall_Street_(2013_film)"}
print("Url of the film Encanto :",film_url["Encanto"])

film_year = {"Encanto": "2021",
        "Titanic": "1997",
        "Turning red":"2022",
        "Avatar":"2009",
        "Wolf of Wall Street": "2013" }
print("Release year of the film Encanto :",film_year["Encanto"])

starring_Encanto = ["Stephanie Beatriz", "Maria Cecilia Botero", "John Leguizamo", "Mauro Castillo"]
starring_Titanic = ["Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates", "Frances Fisher"]
starring_Turning_Red = ["Rosalie Chiang", "Sandra Oh", "Ava Morse", "Hyein Park", "Orion Lee"]
starring_Avatar = ["Sam Worthington", "Zoe Saldana", "Stephen Lang", "Michelle Rodriguez", "Sigourney Weaver" ]
starring_Woll_of_Wall_Street = ["Leonardo DiCaprio", "Jonah Hill", "Margot Robbie", "Matthew McConaughey", "Kyle Chandler"]

film_starring = {"Encanto": starring_Encanto,
        "Titanic": "1997",
        "Turning red":"NaN",
        "Avatar":"2009",
        "Wolf of Wall Street": "2013" }
print("Film starring Encanto :",film_starring["Encanto"])