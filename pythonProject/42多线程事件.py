# 事件：线程之间的通信

import threading, time

class Boss(threading.Thread):
    def run(self):
        print("BOSS：从现在开始咱们就要996了，欢呼吧")
        # 事件设置
        print(event.isSet())
        event.set()
        time.sleep(10)
        print("BOSS：大家干完活了，以后就不996了")
        print(event.isSet())
        event.set()
        pass
a = 1
class Worker(threading.Thread):
    def run(self):
        event.wait()
        print("Worker：哎妈呀，咋还996了呢，命这么苦，抓紧干吧")
        print(event, end=" ")
        print(event.isSet())
        event.clear()
        print(event, end=" ")
        print(event.isSet())
        global a
        a = a + 1
        print(a)
        print(event.isSet())
        event.wait()
        print("Worker：Oh，Yeah")
        pass

if __name__ == "__main__":
    # 先执行这个
    event = threading.Event()
    threads = []
    for i in range(5):
        threads.append(Worker())
        pass
    threads.append(Boss())
    for t in threads:
        t.start()
        pass
