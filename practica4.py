import random
import pickle


class aprox:
    def __init__(self, alpha):
        self.ram = []
        self.alpha = alpha
        self.aprox_r = 0
        self.aprox_e = 0
        self.load_data()
        self.aprox_real()
        self.aprox_heuristic()

    def gen_data(self):
        for x in range(0, 500):
            self.ram.append(random.randrange(101))
        rand = open('data.txt', 'w')
        pickle.dump(self.ram, rand)

    def load_data(self):
        data = open('data.txt', 'r')
        self.ram = pickle.load(data)

    def aprox_real(self):
        prom = 0.0
        n = 0
        for data in self.ram:
            if n == 0:
                prom = data
                n = n + 1
            else:
                prom = round((prom * n + data) / (n + 1), 4)
                n = n + 1
        self.aprox_r = prom
        return self.aprox_r

    def aprox_heuristic(self):
        prom = 0.0
        n = 0
        for data in self.ram:
            if n == 0:
                prom = data
                n = n + 1
            else:
                prom = round((self.alpha * prom + (1 - self.alpha) * data), 4)

        self.aprox_e = prom


r = aprox(0.5)
r.gen_data()
