import random

def random_char():
    if random.randint(1,2) % 3 == 0:
        return chr(random.randint(65,90))
    elif random.randint(1,2) % 3 == 1:
        return chr(random.randint(97,122))
    return ' '

def random_string(length):
    random_string = ' '*length
    
    for i in range(len(random_string)):
        random_string = random_string[:i]+random_char()+random_string[i+1:]

    return random_string

def split(word): 
    return [char for char in word]

def listToString(stringList):
    string = "" 
    return string.join(stringList)

class DNA():
    def __init__(self, n):
        self.genes = split(random_string(n))
        self.fitness = 0

    def calcFitness(self, target):
        score = 0
        for i in range(len(self.genes)):
            if self.genes[i] == target[i]:
                score += 1
        self.fitness = score / len(target)

    def crossover(self, partner):
        child = DNA(len(self.genes))
        midpoint = random.randint(0,len(self.genes)-1)

        for i in range(len(self.genes)):
            if i > midpoint:
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = partner.genes[i]
        return child

    def mutate(self, mutationRate):
        for i in range(len(self.genes)):
            if random.random() < mutationRate:
                self.genes[i] = random_char()

def average_fitness(population):
    total = 0
    for x in population:
        total += x.fitness
    return total/len(population)

def fittest_guy(population):
    fittest = population[0]
    for x in population:
        if x.fitness > fittest.fitness:
            fittest = x
    return fittest

def new_generation(population):
    matingPool = []
    for i in range(totalPopulation):
        for j in range(int(population[i].fitness * 100)):
            matingPool.append(population[i])

    for i in range(totalPopulation):
        parentA = matingPool[random.randint(0,len(matingPool)-1)]
        parentB = matingPool[random.randint(0,len(matingPool)-1)]
        child = parentA.crossover(parentB)
        child.mutate(mutationRate)
        population[i] = child
        population[i].calcFitness(target)

mutationRate = 0.01
totalPopulation = 150
target = 'lezy jerzy na wiezy';

population = []

for i in range(totalPopulation):
    nowy = DNA(len(target))
    population.append(nowy)
    population[i].calcFitness(target)

generation = 0

while listToString(fittest_guy(population).genes) != target:
    new_generation(population)
    generation += 1
    print('Current generation: ', generation)
    print(listToString(fittest_guy(population).genes))

