import threading
import time
from State import *
from Clock import Clock
from Button import Button


# Function to simulate time ticking
def display_time(clock, delay):
    while True:
        time.sleep(delay)
        if clock.is_alarm() == False:
            print("Time:", clock.time)
        elif clock.is_alarm() == True:
            print("Alarm!")

# Function to simulate other tasks
def listen_input(button, delay):
    print("press 's' for short press and 'l' for long press: ")
    while True:
        time.sleep(delay)
        press_type = input()
        if press_type=="s" or press_type=="l":
            button.notify(press_type)
            press_type = ""

if __name__ == "__main__":
    button = Button()
    normal_mode = NormalMode()
    clock = Clock(normal_mode)
    button.attach(clock)

    # do display_time every 1 sec
    time_thread = threading.Thread(target=display_time, args=(clock, 1))
    time_thread.daemon = True
    time_thread.start()

    time.sleep(0.5)
    # do listen_input every 1 sec
    tasks_thread = threading.Thread(target=listen_input, args=(button, 1))
    tasks_thread.daemon = True
    tasks_thread.start()
