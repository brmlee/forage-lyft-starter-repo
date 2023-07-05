from abc import ABC

from car import Car
class SpindlerBattery(Car, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def battery_should_be_serviced(self):
        return self.curret_date - self.last_service_date > 2
