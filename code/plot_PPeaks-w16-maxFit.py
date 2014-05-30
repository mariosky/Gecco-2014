from pylab import *
import itertools, operator
import os

homogeneous_file = "data/PPeaks-w16-200-Homogeneo-p300.dat"

homogeneous = open(homogeneous_file)
fitness = [ line.split(",") for line in homogeneous if len(line.split(",")) > 3 ]

#best_runs = [ (int(list[-1].split(':')[-1]),  list[0], list[1], float(list[3]), list[1],list[-5:]) for list in fitness if  float(list[3]) == 1.0]
#print "BEST:",min(best_runs)

#for r in best_runs:
#    print r

#Hall of Fame
#(397, '33', '9', 1.0, '9', ['0.535210726428', '0.763335658718', '16', '6', 'pop:sample:397\n']) 96.13
#(339, '2', '6', 1.0, '6', ['0.48457002759', '0.826456281903', '12', '9', 'pop:sample:339\n'])  82 Seg


all_runs = [ (int(list[-1].split(':')[-1]),  list[0], list[1], float(list[3]), list[1],list[-5:]) for list in fitness]
all_runs.sort()

avg_homogeneous = []
for key, group in itertools.groupby(all_runs, key=operator.itemgetter(0)):
    rows = [float(row[3]) for row in group] #row[3] = fitness
    avg_homogeneous.append((key, max(rows),std(rows)/sqrt( len(rows))))
avg_homogeneous = array(avg_homogeneous)


heterogeneous_file = "data/PPeaks-w16-20-Heterogeneo.dat"
heterogeneous = open(heterogeneous_file)
fitness_heterogeneous = [ line.split(",") for line in heterogeneous if len(line.split(",")) > 3 ]

_runs = [ (int(list[-1].split(':')[-1]),  list[0], list[1], float(list[3]), list[1],list[-5:]) for list in fitness_heterogeneous]
_runs.sort()

avg_heterogenous = []
for key, group in itertools.groupby(_runs, key=operator.itemgetter(0)):
    rows = [float(row[3]) for row in group] #row[3] = fitness
    avg_heterogenous.append((key, max(rows) , std(rows)/sqrt(len(rows)) ))

avg_heterogenous = array(avg_heterogenous)


heterogeneous_best_file = "data/PPeaks-w16-20-HomogeneoBest-p300.dat"
heterogeneous_best = open(heterogeneous_best_file)
fitness_heterogeneous_best = [ line.split(",") for line in heterogeneous_best if len(line.split(",")) > 3 ]

_runs_best = [ (int(list[-1].split(':')[-1]),  list[0], list[1], float(list[3]), list[1],list[-5:]) for list in fitness_heterogeneous_best]
_runs_best.sort()

avg_heterogenous_best = []
for key, group in itertools.groupby(_runs_best, key=operator.itemgetter(0)):
    rows = [float(row[3]) for row in group] #row[3] = fitness
    avg_heterogenous_best.append((key, max(rows) , std(rows)/sqrt(len(rows)) ))

avg_heterogenous_best = array(avg_heterogenous_best)



fig = figure()
ax1 = fig.add_subplot(111)

plt.plot(avg_homogeneous[:400,0], avg_homogeneous[:400,1],'b',linewidth = 1)
plt.plot(avg_heterogenous[:400,0], avg_heterogenous[:400,1],'r',linewidth = 1)
plt.plot(avg_heterogenous_best[:400,0], avg_heterogenous_best[:400,1],'g',linewidth = 1)

#plt.errorbar( avg_homogeneous[:400,0],  avg_homogeneous[:400,1],  yerr=avg_homogeneous[:400,2], fmt='b-',linewidth = 1)
#plt.errorbar(avg_heterogenous[:400,0], avg_heterogenous[:400,1], yerr=avg_heterogenous[:400,2], fmt='r-',linewidth = 1)

plt.legend(( 'Average Homogeneous','Average Heterogeneous',  'Best Homogeneous '),
           'lower right', shadow=True)







ax1.set_axisbelow(True)
ax1.set_title('16 Workers, P-Peaks')
ax1.set_xlabel('Sample number')
ax1.set_ylabel('Fitness')

plt.savefig('plots/PPeaks-w16-MAX.eps')

homogeneous.close()
heterogeneous.close()
heterogeneous_best.close()
