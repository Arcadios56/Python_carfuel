class Carfuel:
    def __init__(self, fuel_efficiency):
        self.is_running = False
        self.fuel_level = 0.0
        self.MAX_FUEL_CAPACITY = 50.0
        self.FUEL_EFFICIENCY = fuel_efficiency

    def start(self):
        if not self.is_running and self.fuel_level > 0:
            self.is_running = True
            return True
        return False

    def stop(self):
        self.is_running = False

    def refuel(self, liters):
        if liters > 0 and (self.fuel_level + liters) <= self.MAX_FUEL_CAPACITY:
            self.fuel_level += liters
            return True
        return False

    def drive(self, distance):
        if self.is_running and distance > 0:
            fuel_needed = distance / self.FUEL_EFFICIENCY
            if fuel_needed <= self.fuel_level:
                self.fuel_level -= fuel_needed
                return True

        return False
        
    def check_state(self):
        running_status = "running" if self.is_running else "stopped"
        return f"Car State: {running_status}, Fuel Level: {self.fuel_level:.2f} liters"
