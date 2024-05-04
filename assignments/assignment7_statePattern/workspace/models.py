import threading
import time

# Interface for the Subscriber
class Subscriber:
    def update(self, context):
        pass

# Interface for the State
class State:
    def long_press(self):
        pass

    def short_press(self):
        pass

# Concrete State classes
class NormalMode(State):
    def long_press(self):
        print("Switching to Preset Mode")

    def short_press(self):
        print("Incrementing time")

class PresetMode(State):
    def long_press(self):
        print("Switching to Countdown Mode")

    def short_press(self):
        print("Decreasing time")

class CountdownMode(State):
    def long_press(self):
        print("Switching to Normal Mode")

    def short_press(self):
        print("Setting countdown time")

# Clock class
class Clock:
    def __init__(self, initial_state):
        self.state = initial_state
        self.observers = []
        self.time = 0

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def change_state(self, state):
        self.state = state

    def long_press(self):
        self.state.long_press()

    def short_press(self):
        self.state.short_press()

# Button class
class Button:
    def __init__(self, clock):
        self.clock = clock

    def attach(self, observer):
        self.clock.attach(observer)

    def detach(self, observer):
        self.clock.detach(observer)

    def notify(self):
        self.clock.notify()

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
