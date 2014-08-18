__author__ = 'mariosky'

from pylab import *
import itertools, operator
import os


w1_file = open("data/one_max-w2-24-p64-1408138731.dat")
w3_file = open("data/one_max-w3-64-p200-1408042361.dat")
w4_file = open("data/one_max-w4-64-p200-1408042096.dat")
w6_file = open("data/one_max-w6-32-p200-1408041864.dat")


files = [w1_file, w3_file, w4_file, w6_file]
# multiple box plots on one figure

records = [[ map(float,line.split(',')[:-6]) for line in f if len(line.split(",")) > 3 ] for f in files ]

print records
data = []

for dataset in records:
    recs = []
    for key, group in itertools.groupby(dataset, key=operator.itemgetter(0)):
        recs.append( sum([row[9] for row in group]))
    data.append(recs)


print map(len,data)

# multiple box plots on one figure
fig = figure()
ax1 = fig.add_subplot(111)

bp = plt.boxplot(data)

ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
               alpha=0.5)

# Hide these grid behind plot objects
ax1.set_axisbelow(True)
ax1.set_title('Evaluations to solution. One-Max 128 bits')
ax1.set_xlabel('%s Workers')
ax1.set_ylabel('Number of evaluations')

xtickNames = plt.setp(ax1, xticklabels= ["w1s64","w3s64","w4s64","w6s32"]  )
plt.setp(xtickNames)

plt.savefig('one_max_plot_evaluations_evospace.eps')
map(file.close, files)
