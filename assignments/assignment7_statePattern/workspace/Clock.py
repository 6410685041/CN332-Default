import time
import threading

# Interface for the Subscriber
class Subscriber:
    def update(self, context):
        pass

# Clock class
class Clock(Subscriber):
    def __init__(self, initial_state=None):
        self.state = initial_state
        self.observers = []
        self.alarm = False
        self.time = 0
        self.countdown_time = 60
        self.start_tick()
        self.temp = self.time

    def update(self, press_type: str):
        if press_type == "s":
            self.short_press()
        elif press_type == "l":
            self.long_press()

    def change_state(self, state):
        self.state = state

    def long_press(self):
        self.change_state(self.state.long_press())

    def short_press(self):
        self.change_state(self.state.short_press())
        
    def print_time(self):
        hours = (self.time // 3600) % 24
        minutes = (self.time // 60) % 60
        seconds = self.time % 60
        
        # Print in hh:mm:ss format
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        
    def get_time(self):
        return self.time
    
    def set_time(self, time):
        self.time = time
        
    def start_tick(self):
        time_thread = threading.Thread(target=self.tick)
        time_thread.daemon = True
        time_thread.start()
    
    def tick(self):
        while True:
            time.sleep(1)
            self.time += 1
        
    # Alarm related methods    
    def alarm_on(self):
        self.alarm = True
        
    def alarm_off(self):
        self.alarm = False
        
    def is_alarm(self):
        return self.alarm
    
    def start_countdown(self):
        self.countdown_time = 5
        time_thread = threading.Thread(target=self.countdown)
        time_thread.daemon = True
        time_thread.start()
    
    def countdown(self):
        while self.countdown_time > 0:
            time.sleep(1)
            self.countdown_time -= 1
        self.alarm_on()
        
    def print_countdown_time(self):
        print(f"Countdown: {self.countdown_time}")
        
    def get_countdown_time(self):
        return self.countdown_time
    
    def on_preset(self):
        self.temp = self.time

    def increase_temp(self):
        # add 1 minute
        self.temp += 60

    def print_temp(self):
        hours = (self.temp // 3600) % 24
        minutes = (self.temp // 60) % 60
        seconds = self.temp % 60
        
        # Print in hh:mm:ss format
        print(f"{hours:02}:{minutes:02}:{seconds:02}")