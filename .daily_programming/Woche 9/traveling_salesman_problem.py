from itertools import permutations

# Funktion zur Berechnung der Gesamtdistanz einer Route
def calculate_total_distance(route, distances):
    total_distance = 0
    for i in range(len(route) - 1):
        # Addiere die Entfernung zwischen aufeinanderfolgenden Städten in der Route
        total_distance += distances[route[i]][route[i + 1]]
    
    # Füge die Entfernung von der letzten Stadt zur Startstadt hinzu
    total_distance += distances[route[-1]][route[0]]  # zurück zur Startstadt
    return total_distance

# Funktion für das Brute-Force-Verfahren des Handelsreisendenproblems
def traveling_salesman_bruteforce(distances):
    num_cities = len(distances)
    
    # Generiere alle möglichen Permutationen der Stadtindizes
    all_routes = list(permutations(range(num_cities)))

    min_distance = float('inf')  # Initialisiere mit einer unendlich großen Distanz
    best_route = None

    # Iteriere über alle generierten Routen
    for route in all_routes:
        # Berechne die Gesamtdistanz der aktuellen Route
        distance = calculate_total_distance(route, distances)
        
        # Aktualisiere die beste Route und die minimale Distanz, falls eine bessere Route gefunden wurde
        if distance < min_distance:
            min_distance = distance
            best_route = route

    return best_route, min_distance

# Beispielstädte und Entfernungen
cities = ["Stadt A", "Stadt B", "Stadt C"]
distances = [
    [0, 10, 15],
    [10, 0, 20],
    [15, 20, 0]
]

# Anwendung der Funktion für das Handelsreisendenproblem
best_route, min_distance = traveling_salesman_bruteforce(distances)

# Ausgabe der Ergebnisse
print("Beste Route:", best_route)
print("Minimale Entfernung:", min_distance)
