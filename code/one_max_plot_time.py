__author__ = 'mariosky'



from pylab import *


w1_file = open("data/one_max-w2-24-p64.dat")
w3_file = open("data/one_max-w3-18-p64.dat")
w4_file = open("data/one_max-w4-12-p64.dat")
w6_file = open("data/one_max-w6-8-p52.dat")



w1_time = [ map(float,line[:-1].split(","))[1] for line in w1_file if len(line.split(",")) == 3 ]
w3_time = [ map(float,line[:-1].split(","))[1] for line in w3_file if len(line.split(",")) == 3 ]
w4_time = [ map(float,line[:-1].split(","))[1] for line in w4_file if len(line.split(",")) == 3 ]
w6_time = [ map(float,line[:-1].split(","))[1] for line in w6_file if len(line.split(",")) == 3 ]


data = [w1_time, w3_time, w4_time, w6_time]
# multiple box plots on one figure



fig = figure()
ax1 = fig.add_subplot(111)

bp = plt.boxplot(data)

ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
               alpha=0.5)

# Hide these grid behind plot objects
ax1.set_axisbelow(True)
ax1.set_title('Time (in seconds) to solution. 128 bits')
ax1.set_xlabel('Number of workers')
ax1.set_ylabel('Time in seconds')

xtickNames = plt.setp(ax1, xticklabels= ["w1s64","w3s64","w4s64","w6s32"] )
#plt.setp(xtickNames, rotation=45, fontsize=8)
plt.setp(xtickNames)
#show()
plt.savefig('one_max_plot_time_evospace.eps')

w1_file.close()
w3_file.close()
w4_file.close()
w6_file.close()


