planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")

planet_list.extend(["Uranus", "Neptune"])

planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")

planet_list.append("Pluto")

print(planet_list)

rocky_planets = planet_list[0:3]

print(rocky_planets)
print(planet_list)

del planet_list[8]
print(planet_list)

spacecraft_visits = [
    ("MESSENGER", ["Mercury", "Venus"]),
    ("Galileo", ["Venus", "Jupiter"]),
    ("Magellan", ["Venus"]),
    ("Cassini", ["Venus", "Jupiter", "Saturn"]),
    ("Mariner 2", ["Venus"]),
    ("Mariner 5", ["Venus"]),
    ("Mariner 4", ["Mars"]),
    ("Mariner 6", ["Mars"]),
    ("Mariner 7", ["Mars"]),
    ("Mariner 9", ["Mars"]),
    ("Mariner 10", ["Mercury", "Venus"]),
    ("Vega 1", ["Venus"]),
    ("Vega 2", ["Venus"]),
    ("Venera 1", ["Venus"]),
    ("Venera 2", ["Venus"]),
    ("Venera 3", ["Venus"]),
    ("Venera 4", ["Venus"]),
    ("Venera 5", ["Venus"]),
    ("Venera 6", ["Venus"]),
    ("Venera 7", ["Venus"]),
    ("Venera 8", ["Venus"]),
    ("Venera 9", ["Venus"]),
    ("Venera 10", ["Venus"]),
    ("Venera 11", ["Venus"]),
    ("Venera 12", ["Venus"]),
    ("Venera 13", ["Venus"]),
    ("Venera 14", ["Venus"]),
    ("Venera 15", ["Venus"]),
    ("Venera 16", ["Venus"]),
    ("Venus Express", ["Venus"]),
    ("Viking 1", ["Mars"]),
    ("Viking 2", ["Mars"]),
    ("Mars Odyssey", ["Mars"]),
    ("Mars Pathfinder", ["Mars"]),
    ("New Horizons", ["Jupiter", "Pluto"]),
    ("Opportunity", ["Mars"]),
    ("Parker Solar Probe", ["Venus"]),
    ("Perseverance", ["Mars"]),
    ("Phoenix", ["Mars"]),
    ("Pioneer 10", ["Jupiter"]),
    ("Pioneer 11", ["Jupiter", "Saturn"]),
    ("Pioneer Venus 1", ["Venus"]),
    ("Pioneer Venus 2", ["Venus"]),
    ("Spirit", ["Mars"]),
    ("Dawn", ["Mars"]),
    ("Curiosity", ["Mars"]),
    ("InSight", ["Mars"]),
    ("Voyager 1", ["Jupiter", "Saturn"]),
    ("Voyager 2", ["Jupiter", "Saturn", "Uranus", "Neptune"]),
    ("Ulysses", ["Jupiter"]),
    ("Juno", ["Jupiter"])
]

for spacecraft, visits in spacecraft_visits:
    print(f"{spacecraft} has visited")
    print("-----------------------")
    for visit in visits:
        print(visit)
    print("")
