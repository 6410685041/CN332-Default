import Clock

# Interface for the State
class State:
    def long_press(self):
        pass

    def short_press(self):
        pass

# Concrete State classes
class NormalMode(State):
    def __init__(self, clock: Clock):
        self.clock = clock
    
    def long_press(self):
        print("Switching to Preset Mode")
        return PresetMode

    def short_press(self):
        print("Switching to Countdown mode and start count down")
        return CountdownMode

class PresetMode(State):
    def __init__(self, clock: Clock):
        self.clock = clock
        
    def long_press(self):
        print("Switching to Normal Mode")
        return NormalMode

    def short_press(self):
        print("Increasing time")
        return PresetMode

class CountdownMode(State):
    def __init__(self, clock: Clock):
        self.clock = clock
    
    def long_press(self):
        print("Didn't do anything")
        return CountdownMode

    def short_press(self):
        print("After alarm is activate, it will stop alarm and switch to NormalMode")
        if self.clock.is_alarm() :
            return NormalMode
        else :
            return CountdownMode
