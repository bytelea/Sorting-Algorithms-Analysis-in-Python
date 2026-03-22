# Sorting Algorithms Analysis in Python
This project was completed as part of the **Algorithms and Data Structures (TU850)** module at TU Dublin.
The aim of the project is to implement and compare five sorting algorithms and analyse how their performance changes as the dataset size increases.

## Project Overview
Sorting algorithms are essential in computer science as they are used to organise data efficiently. In real-world systems, choosing the right algorithm is important because inefficient algorithms can significantly slow down performance as datasets grow.
In this project, five sorting algorithms were implemented from scratch and tested on a real-world dataset of vehicles.

The goal was to:
- Measure execution time of each algorithm
- Compare empirical results with theoretical time complexity
- Analyse scalability and efficiency
- 
## Algorithms Implemented

- **Bubble Sort (O(n²))**
- **Insertion Sort (O(n²))**
- **Selection Sort (O(n²))**
- **Quick Sort (O(n log n))**
- **Merge Sort (O(n log n))**

## Dataset

The dataset represents a **used car inventory**, stored in a CSV file (`vehicles.csv`).

Each record includes:
- Vehicle ID
- Brand
- Model
- Year
- Mileage
- Engine Size
- Price

### Preprocessing
Before sorting:
- Year was converted to integer
- Mileage, Engine Size, Price were converted to floats

This ensures correct numerical comparisons during sorting.

## Experiments

Two main experiments were conducted:

### Sorting by Price (Scalability Test)

Sorting performance was tested with increasing dataset sizes:
250 → 500 → 1000 → 2000 → 8000 → 16000 → 32000 → 64000

Each algorithm was:
- Run 3 times
- Averaged for accuracy
- Tested on the same shuffled dataset

### Sorting by Mileage (Filtered by Year)

The dataset was filtered by year (2020–2024) and sorted by mileage.
This tested how algorithms behave on smaller subsets of data

## Performance Insights
### Key Findings
- **Bubble, Selection, and Insertion Sort**
  - Extremely slow for large datasets
  - Runtime increased dramatically (O(n²))
  - Bubble Sort took **~570 seconds** for 64,000 elements

- **Quick Sort and Merge Sort**
  - Very fast and scalable
  - Maintained low runtime even for large datasets
  - Quick Sort stayed under **0.3 seconds**

## Conclusion

The results clearly show that algorithm efficiency matters.

- Quadratic algorithms (O(n²)) are not suitable for large datasets
- More efficient algorithms (O(n log n)) scale much better
- The experimental results matched theoretical expectations

This project highlights the importance of selecting the right algorithm in real-world systems.
