# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon:
    """ Class that holds a lat/lon """
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon.

class Waypoint:
    def __init__(self, name, lat, lon):
        # Latlon.__init__(self, lat, lon) # Historic way
        super().__init__(lat, lon) # New way
        self.name = name

    def __str__(self):
        return '\nThe %s is located at Longitude: %.2f and Latitude: %.2f and Latitude: %.2f\n' % (self.name, self.lat, self.lon)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

    def _str_(self):
        return '\n%s cache (size: %d, diff: %.1f) is located at Longitude: %.2f and Latitude: %.2f\n' % \
            (self.name, self.size, self.difficulty, self.lat, self.lon)

# Make a new waypoint "Catacombs", 41.70505, -121.51521

w = Waypoint('Catacombs', 41.70505, -121.51521)

# Print it
#
# Without changing the following line, how can you make it print into something
# more human-readable?
print(w)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
g = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(g)
