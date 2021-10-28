import threading, time

condition = threading.Condition()
products = 0

class Producer(threading.Thread):
    def run(self):
        global condition, products
        while True:
            if condition.acquire():
                if products <= 10:
                    products += 1
                    print("{}:{}库存不足商品数量小于等于10，努力生产商品。现在"
                          "商品数量是{}".format("生产者", threading.currentThread().getName(),products))
#                     生产完之后唤醒一个等待的线程继续工作
                    condition.notify() #唤醒一个等待的线程,notifyall唤醒所有
                else:
                    print("{}:{}库存充足商品数量大于10，休息一下。现在"
                          "商品数量是{}".format("生产者", threading.currentThread().getName(),products))
                    condition.wait() #线程等待
                condition.release()#释放锁
                time.sleep(2)
class Consumer(threading.Thread):
    def run(self):
        global condition, products
        while True:
            if condition.acquire():
                if products >= 1:
                    products -= 1
                    print("{}:{}我消费了一件商品,现在商品的数量是{}"
                          .format("消费者",threading.currentThread().getName(),products))
                else:
                    print("{}:{}没有库存了，不卖了，现在商品数量是{}"
                          .format("消费者", threading.currentThread().getName(), products))
                    condition.wait()
                condition.release()
if __name__ == "__main__":
    for i in range(3):
        p = Producer()
        p.start()
    for i in range(10):
        c = Consumer()
        c.start()