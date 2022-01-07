import random

class population:

    def __init__(self, city_population):
        self.prev_sum = 0
        self.pol_dist = {}

        for city, pop in city_population.items():
            self.prev_sum += pop
            self.pol_dist[city] = self.prev_sum

    def get_city(self):

        val =  self.prev_sum * random.random()

        for city, acc_pop in sorted(self.pol_dist.items(), key = lambda x : x[1]):
            if val <= acc_pop:
                return city

obj = population({'sfo': 120.3, 'nyc': 102.56, 'chicago': 23})
print(obj.get_city())