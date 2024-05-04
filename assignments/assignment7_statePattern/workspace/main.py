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
                clock.print_time()
            case "PresetMode":
                clock.print_time()
            case "CountdownMode":
                if clock.is_alarm():
                    print("Alarm!")
                else:
                    clock.print_countdown_time()
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
