import random
from Ant import Ant

TOTAL_CITIES = 100
ITERATIONS = 100
M = 30
ALPHA = 2
BETA = 4
P = 0.4


def born_ants(total_ants, total_cities):
    ants = []
    occupied_cities = []

    for i in range(total_ants):
        city = random.randrange(0, total_cities)
        while city in occupied_cities:
            city = random.randrange(0, total_cities)
        occupied_cities.append(city)
        ant = Ant(city, TOTAL_CITIES)
        ants.append(ant)
    return ants


def generate_distance_matrix(total_cities):
    distance_matrix = []
    min_distance = 5
    max_distance = 50

    for i in range(total_cities):
        row = []
        for j in range(total_cities):
            if i == j:
                row.append(float('inf'))
            else:
                distance = random.randrange(min_distance, max_distance)
                row.append(distance)

        distance_matrix.append(row)
    return distance_matrix


def generate_pheromone_matrix(total_cities):
    initial_pheromone = 1.0
    pheromone_matrix = []

    for i in range(total_cities):
        row = []
        for j in range(total_cities):
            if i == j:
                row.append(0)
            else:
                row.append(initial_pheromone)
        pheromone_matrix.append(row)
    return pheromone_matrix


def update_pheromone_matrix(pheromone_matrix, travelled_ants, total_cities, Lmin):
    for i in range(total_cities):
        for j in range(total_cities):

            if i != j:

                delta = 0
                for ant in travelled_ants[i][j]:
                    delta += Lmin / ant.total_distance
                pheromone_matrix[i][j] = (1 - P) * pheromone_matrix[i][j] + delta
    return pheromone_matrix


def get_Lmin(pheromone_matrix, distance_matrix, travelled_ants, a):
    ant = Ant(0, TOTAL_CITIES)

    for i in range(TOTAL_CITIES):
        ant.walking(pheromone_matrix, distance_matrix, travelled_ants, TOTAL_CITIES, a)

    return ant.total_distance


def get_Lk(pheromone_matrix, distance_matrix):
    counter = 0
    row = 0
    path_distance = 0
    path = [0]

    while counter < len(pheromone_matrix) - 1:
        max = -1
        i_max = -1

        for j in range(len(pheromone_matrix[row])):
            if j not in path and pheromone_matrix[row][j] > max:
                max = pheromone_matrix[row][j]
                i_max = j

        path_distance += distance_matrix[row][i_max]
        row = i_max
        path.append(i_max)
        counter += 1
    return path_distance


def print_distance(distance_matrix, pheromone_matrix):
    counter = 0
    row = 0
    distance = 0
    path = [0]

    while counter < len(pheromone_matrix) - 1:
        max_value = -1
        max_value_index = -1

        for j in range(len(pheromone_matrix[row])):
            if pheromone_matrix[row][j] > max_value and j not in path:
                max_value = pheromone_matrix[row][j]
                max_value_index = j

        distance += distance_matrix[row][max_value_index]
        row = max_value_index
        path.append(max_value_index)
        counter += 1

    print(f"shorter path = {distance}\n")


def main():
    distance_matrix = generate_distance_matrix(TOTAL_CITIES)
    pheromone_matrix = generate_pheromone_matrix(TOTAL_CITIES)

    travelled_ants = [[[] for i in range(TOTAL_CITIES)]
                      for j in range(TOTAL_CITIES)]

    Lmin = get_Lmin(pheromone_matrix, distance_matrix, travelled_ants, 0)
    shortest_path = Lmin
    count = 0

    while count != ITERATIONS:
        pheromone_matrix = generate_pheromone_matrix(TOTAL_CITIES)
        ants = born_ants(M, TOTAL_CITIES)

        for i in range(TOTAL_CITIES):
            for ant_counter in range(len(ants)):
                ants[ant_counter].walking(pheromone_matrix, distance_matrix, travelled_ants, TOTAL_CITIES, ALPHA)
            pheromone_matrix = update_pheromone_matrix(pheromone_matrix, travelled_ants, TOTAL_CITIES, Lmin)

        Lk = get_Lk(pheromone_matrix, distance_matrix)

        print(f"{count+1})\nshortest path = {shortest_path}\nLmin = {Lmin}")

        if Lk < shortest_path:
            print_distance(distance_matrix, pheromone_matrix)
            shortest_path = Lk

        count += 1

    print(f"final shortest path = {shortest_path}")


if __name__ == "__main__":
    main()


























