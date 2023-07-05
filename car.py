from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery, tire1, tire2, tire3, tire4):
        self.engine = engine
        self.battery = battery
        self.tireTR = tire1
        self.tireBR = tire2
        self.tireBL = tire3
        self.tireTL = tire4

    def needs_service(self):
          return self.engine.needs_service() or self.battery.needs_service()