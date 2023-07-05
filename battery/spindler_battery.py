from abc import ABC

from car import Car
class SpindlerBattery(Car, ABC):
    def __init__(self, last_service_date, current_date):
        self.current_date = current_date
        self.last_service_date = last_service_date


    def needs_service(self):
        return self.curret_date - self.last_service_date > 2
