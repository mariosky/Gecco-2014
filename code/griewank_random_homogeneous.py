__author__ = 'mariosky'

import griewank
import cloud, time, yaml, random


config = yaml.load(open("conf/conf.yaml"))

experiment = "w%d-%d-p%d" % (config["NUMBER_OF_WORKERS"], config["RETURN_RATE"]*100,config["POPULATION_SIZE"])
experiment_id = experiment + "-%d" % round(time.time(),0)

datafile = open("data/griewank"+experiment_id+".dat","a")
conf_out = open("conf/griewank"+experiment_id+".yaml","w")
yaml.dump(config, conf_out)
conf_out.close()

for i in range(200):
    config["MUTPB"] = random.random()
    config["CXPB"]  = random.random()
    config["SAMPLE_SIZE"] = random.randint(5,20)
    config["WORKER_GENERATIONS"] = random.randint(5,20)

    start = time.time()
    init_job = cloud.call(griewank.initialize, config=config,  _type=config["WORKER_TYPE"], _env="deap")
    tInitialize = time.time()-start
    print i, tInitialize
    params = [(w, config) for w in range(config["NUMBER_OF_WORKERS"])]

    jids = cloud.map(griewank.work, params, _type=config["WORKER_TYPE"], _depends_on= init_job )
    results_list = cloud.result(jids)

    tTotal = time.time()-start
    totals = "%d,%0.2f,%0.2f,%0.2f,%d,%d" % (i, round(tTotal,2), config["MUTPB"],config["CXPB"],config["SAMPLE_SIZE"],
                                             config["WORKER_GENERATIONS"] )
    print totals
    datafile.write(totals + '\n')
    for worker_list in results_list:
        for data_list in worker_list:
            datafile.write(str(i) +"," + ",".join(map(str,data_list)) + '\n')

