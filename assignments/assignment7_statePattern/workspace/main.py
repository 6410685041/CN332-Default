import threading
import time
from State import *
from Clock import Clock
from Button import Button


# Function to simulate time ticking
def display_time(clock, delay):
    while True:
        time.sleep(delay)
        match str(clock.state):
            case "NormalMode":
                print("Time:", clock.time.strftime("%H:%M:%S"))
            case "PresetMode":
                print("Time:", clock.time.strftime("%H:%M:%S"))
            case "CountdownMode":
                if clock.is_alarm() == False:
                    print("Time:", clock.countdown_time.strftime("%H:%M:%S"))
                elif clock.is_alarm() == True:
                    print("Alarm!")
            case _:
                print("match None")

if __name__ == "__main__":
    button = Button()
    clock = Clock()
    normal_mode = NormalMode(clock)
    clock.change_state(normal_mode)
    button.attach(clock)

    delay = 1

    time_thread = threading.Thread(target=display_time, args=(clock, delay))
    time_thread.daemon = True
    time_thread.start()

    time.sleep(0.5)
    print("press 's' for short press and 'l' for long press: ")
    while True:
        time.sleep(delay)
        press_type = input()
        if press_type=="s" or press_type=="l":
            button.notify(press_type)
            press_type = ""
