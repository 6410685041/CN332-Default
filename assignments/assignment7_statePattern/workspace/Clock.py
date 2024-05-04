import State
import Button

# Interface for the Subscriber
class Subscriber:
    def update(self, context):
        pass

# Clock class
class Clock(Subscriber):
    def __init__(self, initial_state: State):
        self.state = initial_state
        self.observers = []
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