####
#### Local Code based on DEAPs examples:
####

#    This file is part of DEAP.
#
#    DEAP is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of
#    the License, or (at your option) any later version.
#
#    DEAP is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with DEAP. If not, see <http://www.gnu.org/licenses/>.




import random
import time
from math import sin, cos, pi, exp, e, sqrt
from operator import mul
from functools import reduce
import array

from deap import base
from deap import creator
from deap import tools

experiment = "griewank%d-p%d" % (40,512)
experiment_id = experiment + "-%d" % round(time.time(),0)
datafile = open(experiment_id+".dat","a")


# Problem dimension
NDIM = 40

def griewank(individual):
    """Griewank test objective function.

    """
    return 1.0/4000.0 * sum(x**2 for x in individual) - \
        reduce(mul, (cos(x/sqrt(i+1.0)) for i, x in enumerate(individual)), 1) + 1,


creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", array.array, typecode='d', fitness=creator.FitnessMin)



toolbox = base.Toolbox()

toolbox.register("attr_float", random.uniform, -512, 512)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, NDIM)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=0.2, indpb=0.5)
toolbox.register("mate", tools.cxTwoPoints)
toolbox.register("select", tools.selRandom, k=3)
toolbox.register("evaluate", griewank)



# Operator registering

toolbox.register("mutate", tools.mutFlipBit, indpb=0.02)
toolbox.register("select", tools.selTournament, tournsize=4)

def main(i):
    start = time.time()
    pop = toolbox.population(n=100)
    CXPB, MUTPB, NGEN = 0.7, 0.2, 2000

    print "Start of evolution"

    # Evaluate the entire population
    fitnesses = map(toolbox.evaluate, pop)
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    evaluated = len(pop)

    print "Evaluated %i individuals" % evaluated

    # Begin the evolution
    for g in range(NGEN):
        print "-- Generation %i --" % g

        # Select the next generation individuals
        offspring = toolbox.select(pop, len(pop))
        # Clone the selected individuals
        offspring = map(toolbox.clone, offspring)

        # Apply crossover and mutation on the offspring
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        print "  Evaluated %i individuals" % len(invalid_ind)
        evaluated+=len(invalid_ind)
        # The population is entirely replaced by the offspring
        pop[:] = offspring

        # Gather all the fitnesses in one list and print the stats
        fits = [ind.fitness.values[0] for ind in pop]

        #length = len(pop)
        #mean = sum(fits) / length
        #sum2 = sum(x*x for x in fits)
        #std = abs(sum2 / length - mean**2)**0.5

        print "  Min %s" % min(fits)
        print "  Max %s" % max(fits)
        print tools.selBest(pop,1)[0]
        #print "  Avg %s" % mean
        #print "  Std %s" % std

        if min(fits) == 0:
            datafile.write( "%d,%d,%d,%d" % (i,g, time.time()-start, evaluated))
            break





if __name__ == "__main__":
    for i in range(1):
        main(i)