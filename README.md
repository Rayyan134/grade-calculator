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

# Refactor Grade Calculator with NumPy

## Version Comparison

Pure Python:
- Uses loops and conditionals
- ~150 lines

NumPy:
- Uses vectorised operations
- ~50 lines
- Faster and more concise

This project was refactored to learn NumPy and data-analysis workflows.



## A few NumPy concepts worth remembering from this project:

```Python
grades >= 90
```

Creates a Boolean array:
```Python
[True, False, True, False]
```



```Python
np.sum(grades >= 90)
```

Counts the "True" values because:
```Python
True = 1
False = 0
```



```Python
np.mean(grades >= 60)
```

Calculates the fraction of passing students:
```Python
[True, True, False, True] --> [1, 1, 0, 1]

mean = 0.75
```

which becomes:
```Python
0.75 * 100 = 75%
```

That's one of the most useful NumPy tricks to remember because it replaces loops with vectorised operations.







# How the Grade Distribution Works

Instead of:
```Python
for grade in grades:

  if grade >= 90:
    ...
```

NumPy evaluates the entire array at once:
```Python
grades >= 90
```

Example:
```Python
grades = np.array([85, 92, 77, 95, 68])
```

Produces:
```Python
[False True False True False]
```

Then:
```Python
np.sum(grades >= 90)
```

Becomes:
```Python
0 + 1 + 0 + 1 + 0
```

Result:
```Python
2
```

No loops written



# Original vs NumPy

## Original
```Python
read_students

calculate_mean

calculate_median

grade_distribution

write_results

main
```

≈ 150 lines including comments and docstrings.

## NumPy Version
```Python
read_grades

write_results

main
```

≈ 40–60 lines.

## What the Original Implementation Taught:
* Functions
* Loops
* Conditionals
* Dictionaries
* CSV files
* Code organisation

## What the NumPy Implementation Taught:
* Vectorisation
* Boolean masking
* Array operations
* Statistical functions
* Data-analysis style programming
