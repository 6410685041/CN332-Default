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

    def __str__(self):
        return "NormalMode"
    
    def long_press(self):
        print("Switching to Preset Mode")
        return PresetMode(clock=self.clock)

    def short_press(self):
        print("Switching to Countdown mode and start count down")
        return CountdownMode(clock=self.clock)

class PresetMode(State):
    def __init__(self, clock: Clock):
        self.clock = clock
        self.clock.on_preset()
        self.clock.set = True

    def __str__(self):
        return "PresetMode"
        
    def long_press(self):
        print("Switching to Normal Mode")
        self.clock.set_time(self.clock.temp)
        self.clock.set = False
        return NormalMode(clock=self.clock)

    def short_press(self):
        print("Increasing time")
        self.clock.increase_temp()
        return PresetMode(clock=self.clock)

class CountdownMode(State):
    def __init__(self, clock: Clock):
        self.clock = clock
        self.clock.start_countdown()

    def __str__(self):
        return "CountdownMode"
    
    def long_press(self):
        print("Didn't do anything")
        return CountdownMode(clock=self.clock)

    def short_press(self):
        print("After alarm is activate, it will stop alarm and switch to NormalMode")
        if self.clock.is_alarm():
            self.clock.alarm_off()
            return NormalMode(clock=self.clock)
        else :
            return CountdownMode(clock=self.clock)
