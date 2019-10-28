# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        pass
 
latlon1 = LatLon(50, -123)
print(f"Lattitude: {latlon1.lat}, Longitude: {latlon1.lon}")

        
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name
        pass
    
    def __str__(self):
        return "Waypoint name: " + self.name + " at lattitude: " + str(self.lat) + " and longitude: " + str(self.lon)

wp1 = Waypoint("bobby", 24, -130)
print(f"Waypoint:\n\tname: {wp1.name}\n\tlat: {wp1.lat}\n\tlon: {wp1.lon}")

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return "Geocache name: " + self.name + " with difficulty: " + str(self.difficulty) + " and size: " + str(self.size) + " at lattitude: " + str(self.lat) + ", longitude: " + str(self.lon)

gc1 = Geocache("bobby", 5, 3, 24, -130)
print(f"Waypoint:\n\tname: {gc1.name}\n\tdifficulty: {gc1.difficulty}\n\tsize: {gc1.size}\n\tlat: {gc1.lat}\n\tlon: {gc1.lon}")

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint = Waypoint("Catacombs", 41.70505, -121.51521)
print(f"Waypoint:\n\tname: {waypoint.name}\n\tlat: {waypoint.lat}\n\tlon: {waypoint.lon}")

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(geocache)
