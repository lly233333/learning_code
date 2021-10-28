# 多线程方法
import threading
import random
import time

num = 10000
def my_print(info):
    time.sleep(random.randint(1, 10))
    print("执行事件" + info)
    global num
    num = num -1
    print(num)
    pass
# 注意main两边的下划线
if __name__ == "__main__":
    # 新建一个线程，并且执行对应的任务
    # 函数当作参数传入时候，不能加（）
    t1 = threading.Thread(target=my_print, args=("线程1",))
    t2 = threading.Thread(target=my_print, args=("线程2",))
    t3 = threading.Thread(target=my_print, args=("线程3",))
    # 调用线程
    t1.start()
    t2.start()
    t3.start()
    # main是主线程，t1是子线程
    print("do something")
    pass
