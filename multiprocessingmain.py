from board import *
import time 
import os 
# from multiprocessing import Pool, cpu_count
import multiprocessing as mp 

# np.random.seed(0)
# collision = []
bdsize = 100000
# fastest = None 
# print(bd.collisions) 
# def run(seed):
#     np.random.seed(seed)
#     bd = board(bdsize, randinit=False,threshold=10)
#     bd.repair(withprogressbar=False) 

def worker(i, quit, foundit, ccnt):
    if ccnt == 1:
        pb = True
    else:
        pb = False 
    # global fastest
    print ("process %d started" % i)
    while not quit.is_set():
        np.random.seed(i)
        bd = board(bdsize, randinit=False,threshold=10,with_progressbar_when_initializing=pb)
        bd.repair(withprogressbar=pb) 
        foundit.set()
        # print(bd.collisions)
        # fastest = bd.collisions 
        
        break 
    print ("process %d is done" % i)


tic = time.perf_counter()
if bdsize < 5000000 or mp.cpu_count() < 4:
    ccnt = 1
else:
    ccnt = mp.cpu_count()/2
# ccnt = mp.cpu_count() 
# ccnt = 8
quit = mp.Event()
foundit = mp.Event()
for i in range(ccnt):
    p = mp.Process(target=worker, args=(i, quit, foundit, ccnt))
    p.start()
foundit.wait()
quit.set()

toc = time.perf_counter()
# bd.printall(bd=True, attack=True)

# print(bd.collisions)
# print("total iteration = {}".format(bd.iter_num))
# print(bd.collisions)
print("time = {:.2f}s".format(toc - tic))






