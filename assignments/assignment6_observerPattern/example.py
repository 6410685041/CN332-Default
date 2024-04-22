class VehicleDetectionSystem:
    def __init__(self):
        self.observers = []
        self.vehicles_count = 0

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self.vehicles_count)

    def detect_vehicle(self):
        self.vehicles_count += 1
        self.notify()

class Observer:
    def update(self, count):
        pass

class TrafficManagementSystem(Observer):
    def update(self, count):
        print(f"Traffic Management System: Vehicle count updated to {count}. Adjusting traffic signals accordingly.")

class SecurityMonitoringSystem(Observer):
    def update(self, count):
        print(f"Security Monitoring System: Vehicle count updated to {count}. Scanning for security threats.")

class DataAnalyticsSystem(Observer):
    def update(self, count):
        print(f"Data Analytics System: Vehicle count updated to {count}. Analyzing traffic patterns.")

class Client:
    def __init__(self, detection_system):
        self.detection_system = detection_system

    def setup_observers(self):
        traffic_management = TrafficManagementSystem()
        security_monitoring = SecurityMonitoringSystem()
        data_analytics = DataAnalyticsSystem()
        self.detection_system.attach(traffic_management)
        self.detection_system.attach(security_monitoring)
        self.detection_system.attach(data_analytics)

    def start_detection(self):
        self.detection_system.detect_vehicle()
        self.detection_system.detect_vehicle()

# Example Usage
detection_system = VehicleDetectionSystem()
client = Client(detection_system)
client.setup_observers()
client.start_detection()

