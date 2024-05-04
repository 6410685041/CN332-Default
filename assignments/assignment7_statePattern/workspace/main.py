import threading
import time
from State import NormalMode
from Clock import Clock
from Button import Button


# Function to simulate time ticking
def time_ticker(clock):
    while True:
        time.sleep(1)
        clock.time += 1
        print("Time:", clock.time)
        clock.notify()

# Function to simulate other tasks
def other_tasks(button):
    while True:
        time.sleep(5)
        button.notify()

if __name__ == "__main__":
    normal_mode = NormalMode()
    clock = Clock(normal_mode)
    button = Button(clock)

    # Starting the time ticker thread
    time_thread = threading.Thread(target=time_ticker, args=(clock,))
    time_thread.daemon = True
    time_thread.start()

    # Starting the other tasks thread
    tasks_thread = threading.Thread(target=other_tasks, args=(button,))
    tasks_thread.daemon = True
    tasks_thread.start()

    # Main thread keeps running
    while True:
        pass
