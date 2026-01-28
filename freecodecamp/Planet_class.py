class Planet:
    def __init__(self, name, planet_type, star):
        self.name = name
        self.planet_type = planet_type
        self.star = star
        if not isinstance(name, str) or not isinstance(planet_type, str) or not isinstance(star, str):
            raise TypeError("name, planet type, and star must be strings")
        if name == "" or planet_type == "" or star == "":
            raise ValueError("name, planet_type, and star must be non-empty strings")

    def orbit(self):
        return f"{self.name} is orbitihttps://www.freecodecamp.org/learn/python-v9/workshop-email-simulator/step-1ng around {self.star}..."
    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"
    

planet1 = Planet("Jupiter","Gaseous", "Sol")
planet2 = Planet("Terra","Solid", "Sol")
planet3 = Planet("Mercury","Solid", "Sol")


print(planet1.orbit)
print(planet2.orbit)
print(planet3.orbit)



