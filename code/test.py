__author__ = 'mariosky'

from pylab import *
import itertools, operator

heterogeneous_file = "data/PPeaks-w120-30-Heterogeneo-p1000.dat"
heterogeneous = open(heterogeneous_file)
fitness_heterogeneous = [ line.split(",") for line in heterogeneous if len(line.split(",")) > 3 ]
fitness_max_gens = [line for line in fitness_heterogeneous if int( line[-1].split(":")[-1]) < 1800 ]


heterogeneous_max_fitness= []

for key, group in itertools.groupby(fitness_max_gens, key=operator.itemgetter(0)):
    rows = [float(row[3]) for row in group] #row[3] = fitness
    heterogeneous_max_fitness.append((key, max(rows)))

for i, f in enumerate(heterogeneous_max_fitness):
    print i, f[1]

print "_________________________________________________"

homogeneous_best_file = "data/PPeaks-w120-20-Best.dat"
homogeneous_best = open(homogeneous_best_file)
fitness_heterogeneous_best = [ line.split(",") for line in homogeneous_best if len(line.split(",")) > 3 ]

homogeneous_best_max_gens = [line for line in fitness_heterogeneous_best if int( line[-1].split(":")[-1]) < 1800 ]
homogeneous_max_fitness = []


avg_homogeneous_best = []
for key, group in itertools.groupby(homogeneous_best_max_gens, key=operator.itemgetter(0)):
    rows = [float(row[3]) for row in group] #row[3] = fitness
    homogeneous_max_fitness.append((key, max(rows)))

for i, f in enumerate(homogeneous_max_fitness):
    print i, f[1]
