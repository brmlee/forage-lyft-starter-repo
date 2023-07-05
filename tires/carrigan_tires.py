from tires.tires import Tires


class carriganTire(Tires):
    def __init__(self, tire_array):
        tire_wear_array = tire_array

    def needs_service(self):
        if any(wear >= 0.9 for wear in tire_wear_array):
            return True
           
        else:
            return False