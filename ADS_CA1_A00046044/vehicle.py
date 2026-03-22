class Vehicle: #single vehicle in the dataset
    def __init__(self, vehicle_id, brand, model, year, mileage, engine_size, price):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.year = int(year)
        self.mileage = float(mileage)
        self.engine_size = float(engine_size)
        self.price = float(price)
# stores all the attributes and then converts year to integer and the other values to floats

    def __str__(self): # string representation of the object for when its printing
        return f"{self.brand} {self.model} ({self.year}) - €{self.price}"

# stores and manages the vehicles in one collection
class VehicleCollection:
    def __init__(self): # list to store all the vehicle objects
        self.vehicles = []

    def add_vehicle(self, vehicle): # adds an object into the collection
        self.vehicles.append(vehicle)

    def get_attribute_list(self, attribute): # returns value for specific attribute
        return [getattr(v, attribute) for v in self.vehicles]

    def filter_by_year(self, year): # filters by year
        return [v for v in self.vehicles if v.year == year]