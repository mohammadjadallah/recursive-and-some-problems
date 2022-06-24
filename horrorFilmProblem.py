"""

Example:
Create a simple system for cinema horror films, when the user goes to this cinema before entering to watch the film, the user must enter ID information like full name and age, country, then after that, the system will check if the user is eligible to watch the film or not eligible.

Instructions:
•	Create class attributes as a restricted ages and restricted country.
•	Create instance attributes that will take parameters like age, fullname, country, isMarried.
•	Create instance method that will return a formatted text for the id of the user if age of the user greater than 15 years and his/her country not in restricted countries. Else return this string "Sorry, you are not eligible to watch the horror film".

•	Your output must be like this picture
 

            Name: self.fullname
            Age: self.age
            Is married: self.isMarried
            Country: self.country

        
Sorry, you are not eligible to watch the horror film

"""


# Solution

class HorrorFilm:
    # class attributes 
    restrictedCountry = ["Germany", "United States", "Jordan", "Syria"]
    restrictedAge = 15
    
    # constructor def  __init__() : pass
    def __init__(self, fullname, age, isMarried, country):
        
        # instance attributes
        self.fullname = fullname
        self.age = age
        self.isMarried = isMarried
        self.country = country
        
    def id_of_watcher_horror_film(self):
        identity_information = f"""
            Name: self.fullname
            Age: self.age
            Is married: self.isMarried
            Country: self.country

        """
        # remmber to use class attributes inside the methods you must write in this syntax >> className.classAttribute
        if self.age > HorrorFilm.restrictedAge or self.country.title() not in HorrorFilm.restrictedCountry:
            return identity_information
        else:
            return "Sorry, you are not eligible to watch the horror film"


# create the objects and print the output
watcher1 = HorrorFilm("Mohammad Salem Al Momani", 25, True, "Sweden")
watcher2 = HorrorFilm("Naser Hamed Al Salman", 14, False, "Syria")

print(watcher1.id_of_watcher_horror_film())
print(watcher2.id_of_watcher_horror_film())

"""
Output:


            Name: self.fullname
            Age: self.age
            Is married: self.isMarried
            Country: self.country

        
Sorry, you are not eligible to watch the horror film

"""
