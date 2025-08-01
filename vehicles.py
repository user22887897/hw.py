from abc import ABC, abstractmethod

class Vihicle(ABC):
    _vehicle_count = 0

    def __init__(self, brand : str, model : str, year : int):
        self.brand = brand
        self.model = model
        self.year = year
        Vihicle._vehicle_count += 1

    @abstractmethod
    def get_info(self):
        pass

    @classmethod
    def total_vehicles(cls):
        return cls._vehicle_count

    @property
    def full_name(self):
        return f"{self.brand} {self.model} {self.year}"
    
class Car(Vihicle):
    def init(self, brand: str, model: str, year: int, seats: int):
        super().init(brand, model, year)
        self.seats = seats
    
    def get_info(self) -> str:
        return f"Car: {self.full_name}, Seats: {self.seats}"

class Motorcycle(Vihicle):
    def init(self, brand: str, model: str, year: int, has_sidecar: bool):
        super().init(brand, model, year)
        self.has_sidecar = has_sidecar
    
    def get_info(self) -> str:
        sidecar = "with sidecar" if self.has_sidecar else "without sidecar"
        return f"Motorcycle: {self.full_name}, {sidecar}"