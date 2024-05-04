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
        self.time = time.time()
        self.countdown_time = 60
        
        # time_thread = threading.Thread(target=self.countdown, args=(self, ))
        # time_thread.daemon = True
        # time_thread.start()

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
        print(time.ctime(self.time))
        
    def print_countdown_time(self):
        print(time.ctime(self.countdown_time))
        
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