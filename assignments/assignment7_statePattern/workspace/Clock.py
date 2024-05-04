# Interface for the Subscriber
class Subscriber:
    def update(self, context):
        pass

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