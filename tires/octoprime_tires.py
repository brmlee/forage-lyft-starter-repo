from tires import Tires


class OctoprimeTire(Tires):
    def __init__(self, tire_array):
        tire_wear_array = tire_array
    
    def needs_service(self):
        if sum(tire_wear_array) >= 3:
            return True
        else:
            return False