import sqlite3
from vehicle import Vehicle, Car, Motorcycle

class FleetManager:
    def __init__(self):
        self.conn = sqlite3.connect('fleet.db')
        self.cursor = self.conn.cursor()
    
    def add_vehicle(self, vehicle: Vehicle):
        if isinstance(vehicle, Car):
            self.cursor.execute('''
                INSERT INTO vehicles (type, brand, model, year, seats)
                VALUES (?, ?, ?, ?, ?)
            ''', ('car', vehicle.brand, vehicle.model, vehicle.year, vehicle.seats))
        elif isinstance(vehicle, Motorcycle):
            self.cursor.execute('''
                INSERT INTO vehicles (type, brand, model, year, has_sidecar)
                VALUES (?, ?, ?, ?, ?)
            ''', ('motorcycle', vehicle.brand, vehicle.model, vehicle.year, vehicle.has_sidecar))
        self.conn.commit()
    
    def remove_vehicle(self, brand: str):
        self.cursor.execute('DELETE FROM vehicles WHERE brand = ?', (brand,))
        self.conn.commit()
    
    def update_vehicle(self, brand: str, new_model: str):
        self.cursor.execute('UPDATE vehicles SET model = ? WHERE brand = ?', (new_model, brand))
        self.conn.commit()
    
    def list_vehicles(self):
        self.cursor.execute('SELECT * FROM vehicles')
        vehicles = self.cursor.fetchall()
        for vehicle in vehicles:
            if vehicle[1] == 'car':
                print(f"Car: {vehicle[2]} {vehicle[3]} ({vehicle[4]}), Seats: {vehicle[5]}")
            else:
                sidecar = "with sidecar" if vehicle[6] else "without sidecar"
                print(f"Motorcycle: {vehicle[2]} {vehicle[3]} ({vehicle[4]}), {sidecar}")
    
    def find_vehicle(self, keyword: str):
        self.cursor.execute('''
            SELECT * FROM vehicles 
            WHERE brand LIKE ? OR model LIKE ?
        ''', (f'%{keyword}%', f'%{keyword}%'))
        vehicles = self.cursor.fetchall()
        for vehicle in vehicles:
            if vehicle[1] == 'car':
                print(f"Car: {vehicle[2]} {vehicle[3]} ({vehicle[4]}), Seats: {vehicle[5]}")
            else:
                sidecar = "with sidecar" if vehicle[6] else "without sidecar"
                print(f"Motorcycle: {vehicle[2]} {vehicle[3]} ({vehicle[4]}), {sidecar}")
    
    def close(self):
        self.conn.close()
