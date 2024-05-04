from Clock import Clock

class Button:
    def __init__(self):
        self.myObservers = []
        
    def attach(self, observer) -> None:
        self.myObservers.append(observer)

    def detach(self, observer: Clock) -> None:
        self.myObservers.remove(observer)

    def notify(self, press_type: str) -> None:
        for observer in self.myObservers:
            observer.update(press_type)