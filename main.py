from board import *
import time 
import numpy as np 

np.random.seed(0)
# collision = []
bdsize = 1000
# fastest = None 
# print(bd.collisions) 
# def run(seed):
#     np.random.seed(seed)
#     bd = board(bdsize, randinit=False,threshold=10)
#     bd.repair(withprogressbar=False) 
board_sizes = []
with open ("./nqueens.txt") as file:
    for line in file:
        board_sizes.append(int(line))
print(board_sizes)
with open ("./nqueens_out.txt",'w') as file:
    for i in board_sizes:
        bd = board(i, randinit=False,threshold=10,with_progressbar_when_initializing=True)
        tic = time.perf_counter()
        bd.repair(withprogressbar=True)
        toc = time.perf_counter()
        print("time = {:.2f}s".format(toc - tic))
        print("\ntotal iteration = {}".format(bd.iter_num))
        file.write('[' + ','.join(map(str,bd.bd)) + ']\n')
# bd.printall(bd=True, attack=True)

# print(bd.collisions)

# print(bd.bd)
# print(bd.collisions)







