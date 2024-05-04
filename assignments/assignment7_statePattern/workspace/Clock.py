import State
import Button
import time

# Interface for the Subscriber
class Subscriber:
    def update(self, context):
        pass

# Clock class
class Clock(Subscriber):
    def __init__(self, initial_state: State):
        self.state = initial_state
        self.observers = []
        self.alarm = False
        self.time = 0

    def update(self, press_type: str):
        if press_type == "s":
            self.short_press()
        elif press_type == "l":
            self.long_press()

    def change_state(self, state: State):
        self.state = state

    def long_press(self):
        self.change_state(self.state.long_press())

    def short_press(self):
        self.change_state(self.state.short_press())
        
    def alarm_on(self):
        self.alarm = True
        
    def alarm_off(self):
        self.alarm = False
        
    def is_alarm_on(self):
        return self.alarm