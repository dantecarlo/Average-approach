import random
import pickle


class approach:
    def __init__(self, alpha):
        self.ram = []
        self.alpha = alpha
        self.aprox_r = 0
        self.aprox_e = 0
        # self.gen_data()
        self.load_data()
        # self.aprox_real()
        self.aprox_heuristic()

    def __repr__(self):
        return ("{}".format(self.ram))

    def gen_data(self):
        for x in range(0, 500):
            self.ram.append(random.randrange(101))
        rand = open('data.dat', 'wb')
        pickle.dump(self.ram, rand)

    def load_data(self):
        data = open('data.dat', 'rb')
        self.ram = pickle.load(data)

    def aprox_real(self):
        print("Approach real")
        prom = 0.0
        n = 0
        for data in self.ram:
            if n == 0:
                prom = data
                n = n + 1
            else:
                prom = round((prom * n + data) / (n + 1), 4)
                n = n + 1
            print(prom)

        self.aprox_r = prom
        return self.aprox_r

    def aprox_heuristic(self):
        # print("Approach heuc")
        prom = 0.0
        n = 0
        for data in self.ram:
            if n == 0:
                prom = data
                n = n + 1
            else:
                prom = round((self.alpha * prom + (1 - self.alpha) * data), 4)
            print(prom)

        self.aprox_e = prom


r = approach(0.75)
# print(r)
