from board import *
import time 


np.random.seed(0)
# collision = []
bdsize = 1000
# fastest = None 
# print(bd.collisions) 
# def run(seed):
#     np.random.seed(seed)
#     bd = board(bdsize, randinit=False,threshold=10)
#     bd.repair(withprogressbar=False) 

bd = board(bdsize, randinit=False,threshold=10,with_progressbar_when_initializing=True)
tic = time.perf_counter()
bd.repair(withprogressbar=True)
toc = time.perf_counter()
# bd.printall(bd=True, attack=True)

# print(bd.collisions)
print("\ntotal iteration = {}".format(bd.iter_num))
print(bd.bd)
# print(bd.collisions)
print("time = {:.2f}s".format(toc - tic))






