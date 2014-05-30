__author__ = 'mariosky'


__author__ = 'mariosky'

from pylab import *
import itertools, operator
from scipy import stats
import scipy


heterogeneous_file = "data/PPeaks-w16-20-Heterogeneo.dat"
heterogeneous = open(heterogeneous_file)
fitness_heterogeneous = [ line.split(",") for line in heterogeneous if len(line.split(",")) > 3 ]
fitness_max_gens = [line for line in fitness_heterogeneous if int( line[-1].split(":")[-1]) <= 400 ]


heterogeneous_max_fitness= []

for key, group in itertools.groupby(fitness_max_gens, key=operator.itemgetter(0)):
    rows = [float(row[3]) for row in group] #row[3] = fitness
    heterogeneous_max_fitness.append((key, max(rows)))


print "_________________________________________________"
print "Heterogeneo"
print "_________________________________________________"


heterogeneous = [f for k,f  in heterogeneous_max_fitness]

for f in heterogeneous:
    print f
print "_________________________________________________"


homogeneous_best_file = "data/PPeaks-w16-20-HomogeneoBest-p300.dat"
homogeneous_best = open(homogeneous_best_file)
fitness_heterogeneous_best = [ line.split(",") for line in homogeneous_best if len(line.split(",")) > 3 ]

homogeneous_best_max_gens = [line for line in fitness_heterogeneous_best if int( line[-1].split(":")[-1]) <= 400 ]
homogeneous_max_fitness = []

print "_________________________________________________"
print " HomogeneoBest"
print "_________________________________________________"

avg_homogeneous_best = []
for key, group in itertools.groupby(homogeneous_best_max_gens, key=operator.itemgetter(0)):
    rows = [float(row[3]) for row in group] #row[3] = fitness
    homogeneous_max_fitness.append((key, max(rows)))


homogeneous_best = [f for k,f  in homogeneous_max_fitness]

for f in homogeneous_best:
    print f
print "_________________________________________________"


print "Heterogeneo:    Media, Varianza", stats.mstats.gmean(heterogeneous ), stats.mstats.tvar(heterogeneous)
print "Best Homogeneo: Media, Varianza", stats.mstats.gmean(homogeneous_best ), stats.mstats.tvar(homogeneous_best)

print 'Ranksum:z-statistic  = %6.3f pvalue = %6.4f'% stats.ranksums(heterogeneous,homogeneous_best)
print 'TTest: t-statistic = %6.3f pvalue = %6.4f' % stats.ttest_ind(heterogeneous, homogeneous_best)