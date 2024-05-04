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