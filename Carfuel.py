class Carfuel:
    def __init__(self, fuel_efficiency):
        self.is_running = False
        self.fuel_level = 0.0
        self.MAX_FUEL_CAPACITY = 50.0
        self.FUEL_EFFICIENCY = fuel_efficiency

    def start(tope):
        if not self.is_running and self.fuel_level > 0:
            self.is_running = True
            return True
        return False

    def stop(tope):
        self.is_running = False

    def refuel(tope, liters):
        if liters > 0 and (self.fuel_level + liters) <= self.MAX_FUEL_CAPACITY:
            self.fuel_level += liters
            return True
        return False

    def drive(tope, distance):
        if self.is_running and distance > 0:
            fuel_needed = distance / self.FUEL_EFFICIENCY
            if fuel_needed <= self.fuel_level:
                self.fuel_level -= fuel_needed
                return True
        return False