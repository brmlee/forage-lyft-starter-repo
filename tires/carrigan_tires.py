from tires.tires import Tires


class carriganTire(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        if any(wear >= 0.9 for wear in self.tire_wear):
            return True  
        else:
            return False