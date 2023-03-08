import threading
import time
import random
from collections import deque

def produce(items):
    forever = True
    i = 1
    while forever:
        time.sleep(random.uniform(0, 2))
        items.append(i)
        print("Produced: "+str(i))
        i += 1

def consume(items):
    forever = True
    while forever:
        time.sleep(random.uniform(0, 2))
        if len(items) == 0:
            print("No items to consume.")
            continue
        item = items.popleft()
        print("Consumed: "+str(item))

items = deque([])
producer = threading.Thread(target=produce, args=(items, ))
consumer = threading.Thread(target=consume, args=(items, ))


producer.start()
consumer.start()