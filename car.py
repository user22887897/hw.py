

from fleet.vehicles import Vihicle

class Car(Vihicle):
    def __init__(self, brand, model, year, seats):
        super().__init__(brand, model, year)
        self.seats = seats

    def get_info(self):
        return f"Car {self.full_name} - Seats: {self.seats}"

