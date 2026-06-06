# Grade Calculator

A Python project that reads student grades from a CSV file,
calculates statistics, and writes results to a new CSV file.

## Features

- Read student grades from CSV
- Calculate mean grade
- Calculate median grade
- Calculate grade distribution (A/B/C/D/F)
- Write results to CSV

## Technologies

- Python
- CSV module
- Type hints
- Functions
- Docstrings

## Run

```bash
python main.py
```

## Example Input

students.csv

```csv
name,grade
Ali,85
Fatima,92
Ahmed,77
Sara,95
Yusuf,68
```

## Example Output

results.csv

```csv
metric,value
mean,83.4
median,85
A,2
B,1
C,1
D,1
F,0
```

## Version Comparison

Pure Python:
- Uses loops and conditionals
- ~150 lines

NumPy:
- Uses vectorised operations
- ~50 lines
- Faster and more concise

This project was refactored to learn NumPy and data-analysis workflows.
