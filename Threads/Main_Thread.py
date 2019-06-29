import threading

print("Current running thread is : ", threading.current_thread().getName())

if threading.current_thread() == threading.main_thread():
    print("Main thread")
else:
    print("Some other thread")

'''by Ankush Chavan'''