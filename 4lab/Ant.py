import random
BETA = 4


class Ant:
    def __init__(self, current_city, total_cities):
        self.start_city = current_city
        self.current_city = current_city
        self.visited_cities_count = 1
        self.total_distance = 0
        self.path = [self.current_city]

        self.unvisited_cities = {}
        for i in range(total_cities):
            self.unvisited_cities[i] = True
        self.unvisited_cities[self.current_city] = False

    def walking(self, pheromone_matrix, distance_matrix, travelled_ants, total_cities, a):
        if self.visited_cities_count < total_cities:
            denominator = 0

            for i in range(len(self.unvisited_cities)):
                if self.unvisited_cities[i]:
                    denominator += pow(pheromone_matrix[self.current_city][i], a) * pow((1 / distance_matrix[self.current_city][i]), BETA)
            chances = {}

            for i in range(len(self.unvisited_cities)):
                if self.unvisited_cities[i]:
                    chance = (pow(pheromone_matrix[self.current_city][i], a) * pow((1 / distance_matrix[self.current_city][i]), BETA)) / denominator
                    chances[i] = chance
                else:
                    chances[i] = 0
            discrete_quantity = {}
            discrete_quantity_sum = 0

            for i in range(len(chances)):
                discrete_quantity_sum += chances[i]
                discrete_quantity[i] = discrete_quantity_sum
            random_number = random.uniform(0, discrete_quantity[len(discrete_quantity) - 1])
            previous_city = self.current_city
            next_city = 0

            for i in range(1, len(discrete_quantity)):
                if discrete_quantity[i - 1] < random_number <= discrete_quantity[i]:
                    next_city = i
                    break
            self.current_city = next_city
            if a > 0:
                travelled_ants[previous_city][next_city].append(self)
            self.total_distance += distance_matrix[previous_city][next_city]
            self.visited_cities_count += 1
            self.unvisited_cities[next_city] = False
            self.path.append(next_city)
        else:
            previous_city = self.current_city
            next_city = self.start_city
            self.current_city = self.start_city
            if a > 0:
                travelled_ants[previous_city][next_city].append(self)
            self.total_distance += distance_matrix[previous_city][next_city]
            self.path.append(next_city)
