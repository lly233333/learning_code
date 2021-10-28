import os
from threading import Thread
from multiprocessing import Process

def work():
    # 打印进程号
    print(os.getpid())
    pass
if __name__ == "__main__":
    # 在主进程下开启多个线程，每个线程的PID都一样，所以他们都在一个进程下工作
    t1 = Thread(target=work)
    t2 = Thread(target=work)
    t1.start()
    t2.start()
    print("主进程-》线程 PID", os.getpid())
    # 开启多个进程，每个进程都有独立的PID
    p1 = Process(target=work)
    p2 = Process(target=work)
    p1.start()
    p2.start()
    print("主进程-》进程程 PID", os.getpid())