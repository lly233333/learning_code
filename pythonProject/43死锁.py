import time
from threading import Thread,currentThread,RLock,Lock
# 两个互斥锁对象
# mutexA = mutexB = RLock() 递归锁
# 互斥锁
# mutexA = mutexB = Lock()
mutexA = Lock()
mutexB = Lock()
class House(Thread):
    def room1(self):
        # room1拿住锁A
        mutexA.acquire()
        print(currentThread().getName() + "房间1拿到A锁")
        mutexB.acquire()
        print(currentThread().getName() + "房间1拿到B锁")
        mutexB.release()
        print(currentThread().name + "房间1释放B锁")
        mutexA.release()
        print(currentThread().name + "房间1释放A锁")
        pass
    def room2(self):
        mutexB.acquire()
        print(currentThread().name + "房间2拿到B锁")
        time.sleep(1)
        mutexA.acquire()
        print(currentThread().name + "房间2拿到A锁")
        mutexA.release()
        print(currentThread().name + "房间2释放A锁")
        mutexB.release()
        print(currentThread().name + "房间2释放B锁")
        pass
    def run(self):
        self.room1()
        self.room2()
        pass
if __name__ == "__main__":
    for i in range(10):
        t = House()
        t.run()