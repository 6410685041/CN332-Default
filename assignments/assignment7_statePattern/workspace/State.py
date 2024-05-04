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