import random
from time import sleep

def worker(i, quit, foundit):
    print "%d started" % i
    while not quit.is_set():
        x = random.random()
        if x > 0.7:
            print '%d found %g' % (i, x)
            foundit.set()
            break
        sleep(0.1)
    
    print "%d is done" % i

if __name__ == "__main__":
    import multiprocessing as mp
    quit = mp.Event()
    foundit = mp.Event()
    for i in range(mp.cpu_count()):
        p = mp.Process(target=worker, args=(i, quit, foundit))
        p.start()
    foundit.wait()
    quit.set()