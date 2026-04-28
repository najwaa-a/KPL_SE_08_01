from abc import ABC, abstractmethod

# Kelas abstrak kendaraan
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

# Kelas turunan Car
class Car(Vehicle):
    def start(self):
        return "Mobil menyala"

# Kelas turunan Motorcycle
class Motorcycle(Vehicle):
    def start(self):
        return "Motor senyala"

# Fungsi untuk membuat objek kendaraan
def create_vehicle(vehicle_type):
    if vehicle_type == "Car":
        return Car()
    elif vehicle_type == "Motorcycle":
        return Motorcycle()

# Penggunaan
vehicle1 = create_vehicle("Car")
print(vehicle1.start()) # Output: Mobil menyala

vehicle2 = create_vehicle("Motorcycle")
print(vehicle2.start()) # Output: Motor menyala