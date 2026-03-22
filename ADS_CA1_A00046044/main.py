# imports libraries needed for the project to run
import csv
import random
from vehicle import Vehicle, VehicleCollection
from sorting import *
from experiment import benchmark_sort

def load_data(filename): # loads the dataset from the csv file
    collection = VehicleCollection()

    with open(filename) as file:
        reader = csv.DictReader(file)

        print(reader.fieldnames)

        for row in reader: # loops through each row to create objects
            vehicle = Vehicle(
                row["Vehicle_ID"],
                row["Brand"],
                row["Model"],
                row["Year"],
                row["Mileage"],
                row["Engine_Size"],
                row["Price"]
            )
            collection.add_vehicle(vehicle)
    return collection


# experiment 1: tests sorting performance based on price with increasing dataset sizes
def experiment_by_price(collection):
    sizes = [250, 500, 1000, 2000, 8000, 16000, 32000, 64000]
    prices = collection.get_attribute_list("price")

    for size in sizes: # extracts all price values
        subset = prices[:size]
        random.shuffle(subset) # shuffles to avoid bias

        print(f"\nDataset size: {size}")
        print("Bubble:", benchmark_sort(bubble_sort, subset))
        print("Selection:", benchmark_sort(selection_sort, subset))
        print("Insertion:", benchmark_sort(insertion_sort, subset))
        print("Quick:", benchmark_sort(quick_sort, subset))
        print("Merge:", benchmark_sort(merge_sort, subset))

# experiment 2: test sorting by mileage after filtering by year
def experiment_by_year(collection):
    years = [2020, 2021, 2022, 2023, 2024]

    for year in years:
        filtered = collection.filter_by_year(year)
        mileage = [v.mileage for v in filtered]

        print(f"\nYear: {year}") # benchmarks each sorting algorithm
        print("Bubble:", benchmark_sort(bubble_sort, mileage))
        print("Selection:", benchmark_sort(selection_sort, mileage))
        print("Insertion:", benchmark_sort(insertion_sort, mileage))
        print("Quick:", benchmark_sort(quick_sort, mileage))
        print("Merge:", benchmark_sort(merge_sort, mileage))

def main(): # main function to run the whole program
    collection = load_data("vehicles.csv") # loads the dataset
    experiment_by_price(collection) # runs the experiments
    experiment_by_year(collection)

if __name__ == "__main__":
    main()