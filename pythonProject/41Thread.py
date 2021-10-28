# 多线程类
# 必须继承Thread类

from threading import Thread
class Hello(Thread):
    def __init__(self, name):
        # 调用父类
        super().__init__()
        self.name = name 
    def run(self):
        print("hello%s" %self.name)
    pass
t = Hello("我是一个线程的类")
t.start()
print("我是主线程")