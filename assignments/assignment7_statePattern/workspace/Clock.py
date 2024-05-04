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
            self.state.short_press()
        elif press_type == "l":
            self.state.long_press()

    def attach(self, observer: Button):
        self.observers.append(observer)

    def detach(self, observer: Button):
        self.observers.remove(observer)

    # def notify(self):
    #     for observer in self.observers:
    #         observer.update(self)

    # def change_state(self, state: State):
    #     self.state = state

    # def long_press(self):
    #     self.state.long_press()

    # def short_press(self):
    #     self.state.short_press()