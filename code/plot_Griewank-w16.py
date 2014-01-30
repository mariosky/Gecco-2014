from pylab import *
import itertools, operator
import os

homogeneous_file = "data/griewankw16-100-p300-HomoRand.dat"

homogeneous = open(homogeneous_file)
fitness = [ line.split(",") for line in homogeneous if len(line.split(",")) > 3 ]

best_runs = [ (int(list[-1].split(':')[-1]),  list[0], list[1], float(list[3]), list[1],list[-5:]) for list in fitness if  float(list[3]) <= 0.1]
print "BEST:",min(best_runs)
#
#
for r in best_runs:
    print r
exit()
#Hall of Fame
#(17, '28', '32.41', 0.01, '32.41', ['32.41', '0.57', '0.01', '14', '17\n'])
#(15, '8', '24.62', 0.01, '24.62', ['24.62', '0.19', '0.01', '14', '15\n'])
#(10, '36', '23.67', 0.01, '23.67', ['23.67', '0.56', '0.01', '9', '10\n'])

all_runs = [ (int(list[-1].split(':')[-1]),  list[0], list[1], float(list[3]), list[1],list[-5:]) for list in fitness]
all_runs.sort()

avg_homogeneous = []
for key, group in itertools.groupby(all_runs, key=operator.itemgetter(0)):
    rows = [float(row[3]) for row in group] #row[3] = fitness
    print key, sum(rows)/len(rows), std(rows), len(rows)
    avg_homogeneous.append((key, sum(rows)/len(rows),std(rows)/sqrt( len(rows))))
avg_homogeneous = array(avg_homogeneous)


heterogeneous_file = "data/griewank-hetero-w16.dat"
heterogeneous = open(heterogeneous_file)
fitness_heterogeneous = [ line.split(",") for line in heterogeneous if len(line.split(",")) > 3 ]

_runs = [ (int(list[-1].split(':')[-1]),  list[0], list[1], float(list[3]), list[1],list[-5:]) for list in fitness_heterogeneous]
_runs.sort()

avg_heterogenous = []
for key, group in itertools.groupby(_runs, key=operator.itemgetter(0)):
    rows = [float(row[3]) for row in group] #row[3] = fitness
    print key, sum(rows)/len(rows), std(rows), len(rows)
    avg_heterogenous.append((key, sum(rows)/len(rows) , std(rows)/sqrt(len(rows)) ))

avg_heterogenous = array(avg_heterogenous)


heterogeneous_best_file = "data/griewank-homo-best-w16.dat"
heterogeneous_best = open(heterogeneous_best_file)
fitness_heterogeneous_best = [ line.split(",") for line in heterogeneous_best if len(line.split(",")) > 3 ]

_runs_best = [ (int(list[-1].split(':')[-1]),  list[0], list[1], float(list[3]), list[1],list[-5:]) for list in fitness_heterogeneous_best]
_runs_best.sort()

avg_heterogenous_best = []
for key, group in itertools.groupby(_runs_best, key=operator.itemgetter(0)):
    rows = [float(row[3]) for row in group] #row[3] = fitness
    print key, sum(rows)/len(rows), std(rows), len(rows)
    avg_heterogenous_best.append((key, sum(rows)/len(rows) , std(rows)/sqrt(len(rows)) ))

avg_heterogenous_best = array(avg_heterogenous_best)



fig = figure()
ax1 = fig.add_subplot(111)

up_to = 240
plt.plot(avg_homogeneous[:up_to,0], avg_homogeneous[:up_to,1],'b',linewidth = 1)
plt.plot(avg_heterogenous[:up_to,0], avg_heterogenous[:up_to,1],'r',linewidth = 1)
plt.plot(avg_heterogenous_best[:up_to,0], avg_heterogenous_best[:up_to,1],'g',linewidth = 1)

#plt.errorbar( avg_homogeneous[:400,0],  avg_homogeneous[:400,1],  yerr=avg_homogeneous[:400,2], fmt='b-',linewidth = 1)
#plt.errorbar(avg_heterogenous[:400,0], avg_heterogenous[:400,1], yerr=avg_heterogenous[:400,2], fmt='r-',linewidth = 1)

plt.legend(( 'Average Homogeneous','Average Heterogeneous',  'Best Homogeneous '),
           'upper right', shadow=True)







ax1.set_axisbelow(True)
ax1.set_title('16 Workers, Griewank')
ax1.set_xlabel('Sample number')
ax1.set_ylabel('Fitness')

#plt.savefig('plots/PPeaks-w16.eps')
plt.show()

homogeneous.close()
heterogeneous.close()
heterogeneous_best.close()
