__author__ = 'mariosky'

from multiprocessing import Pool




import one_max
import time, yaml


config = yaml.load(open("conf/conf.yaml"))

experiment = "w%d-%s-p%d" % (config["NUMBER_OF_WORKERS"],"LocalPool",config["POPULATION_SIZE"])
experiment_id = experiment + "-%d" % round(time.time(),0)

datafile = open("data/one_max-"+experiment_id+".dat","a")
conf_out = open("conf/one_max-"+experiment_id+".yaml","w")
yaml.dump(config, conf_out)
conf_out.close()

for i in range(20):
    start = time.time()
    one_max.initialize(config)
    tInitialize = time.time()-start
    print i, tInitialize
    p = Pool(4)
    params = [(w, config) for w in range(config["NUMBER_OF_WORKERS"])]
    start = time.time()
    results = p.map(one_max.work, params)
    #print results

    tTotal = time.time()-start
    totals = "%d,%0.2f,%0.2f" % (i, round(tTotal,2), round(tInitialize,2))
    print totals
    datafile.write(totals + '\n')
    for worker_list in results:
        for data_list in worker_list:
            datafile.write(str(i) +"," + ",".join(map(str,data_list)) + '\n')
