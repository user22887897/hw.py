from vehicle import Car, Motorcycle
from fleet_manager import FleetManager
from database import create_table

def main():
    create_table()
    
    fleet = FleetManager()
    
    car1 = Car("Toyota", "Camry", 2020, 5)
    car2 = Car("Honda", "Civic", 2019, 4)
    moto1 = Motorcycle("Harley-Davidson", "Sportster", 2021, True)
    moto2 = Motorcycle("Yamaha", "MT-07", 2022, False)
    
    fleet.add_vehicle(car1)
    fleet.add_vehicle(car2)
    fleet.add_vehicle(moto1)
    fleet.add_vehicle(moto2)
    
    print("\nВсе транспортные средства:")
    fleet.list_vehicles()
    
    print("\nПоиск по ключевому слову 'Toyota':")
    fleet.find_vehicle("Toyota")
    
    print("\nОбновление модели для Toyota:")
    fleet.update_vehicle("Toyota", "Corolla")
    fleet.list_vehicles()
    
    print("\nУдаление по бренду Honda:")
    fleet.remove_vehicle("Honda")
    fleet.list_vehicles()
    
    fleet.close()

if __name__ == "__main__":
    main()
