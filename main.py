import threading
import time

counter = 0
lock = threading.Lock()

def increment_without_lock():
    global counter
    for _ in range(100000):
        counter += 1

def increment_with_lock():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

print("=== تجربة بدون Lock ===")
counter = 0
t1 = threading.Thread(target=increment_without_lock)
t2 = threading.Thread(target=increment_without_lock)
t1.start()
t2.start()
t1.join()
t2.join()
print(f"النتيجة: {counter} المفروض 200000")

print("\n=== تجربة مع Lock ===")
counter = 0
t1 = threading.Thread(target=increment_with_lock)
t2 = threading.Thread(target=increment_with_lock)
t1.start()
t2.start()
t1.join()
t2.join()
print(f"النتيجة: {counter} صحيحة 100%")
