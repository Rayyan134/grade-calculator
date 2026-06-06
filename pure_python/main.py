# Week 1 FINAL PROJECT:
# Grade Calculator.
# Reads student CSV
# → typed functions with docstrings
# → calculates mean/median/grade distribution
# → writes results CSV
# → proper README + requirements.txt. Push to GitHub.

import csv # allows you to read, parse, and write tabular data (like spreadsheets or databases) in CSV
from statistics import median

# Read CSV

def read_students(
        filename: str
) -> list[dict[str, str]]:
    """
    Read student data from a CSV file.

    Args:
        filename: Path to the CSV file.

    Returns:
        A list of dictionaries containing student data.
    """

    students = []

    # Open the CSV file
    with open(filename, newline="") as file: # purpose of newline="" is to prevent adding extra blank lines

        # Convert each row into a dict
        reader = csv.DictReader(file)

        # Add every row to the students list
        for row in reader:
            students.append(row)

    return students

# Calculate Mean

def calculate_mean(
        grades: list[int]
) -> float:
    """
    Calculate the average grade.

    Args:
        grades: List of student grades.

    Returns:
        Mean grade as a float.
    """

    return sum(grades) / len(grades)

# Calculaute Median

def calculate_median(
        grades: list[int]
) -> float:
    """
    Calculate the median grade.

    Args:
        grades: List of student grades.

    Returns:
        Median grade.
    """

    return median(grades)

# Grade Distribution

def grade_distribution(
        grades: list[int]
) -> dict[str, int]:
    """
    Count how many grades fall into A/B/C/D/F.

    Args:
        grades: List of student grades.

    Returns:
        Dictionary containing grade counts.
    """

    distribution = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "F": 0
    }

    # Check each grade and increment the correct category
    for grade in grades:

        if grade >= 90:
            distribution["A"] += 1 # distribution["A"] is to access the corresponding value from its key

        elif grade >= 80:
            distribution["B"] += 1

        elif grade >= 70:
            distribution["C"] += 1

        elif grade >= 60:
            distribution["D"] += 1

        else:
            distribution["F"] += 1

    return distribution

# Write Results CSV

def write_results(
        filename: str,
        results: dict[str, float | int] # float | int represnts a Union Type, meaning that the value can either be a floating point number or an integer
) -> None:
    """
    Write statistics to a CSV file.

    Args:
        filename: Output CSV filename.
        results: Dictionary containing statistics.
    """

    with open(filename, "w", newline="") as file:

        writer = csv.writer(file) # # csv.writer converts data lists into comma-separated text lines for the file.

        # Header row
        writer.writerow(["metric", "value"])

        # Write every key/value pair
        for metric, value in results.items():
            writer.writerow([metric, value])



# Grade boundaries

"""
90-100 -> A
80-89  -> B
70-79  -> C
60-69  -> D
0-59   -> F
"""

# Example Output CSV (results.csv)

"""
metric,value
mean,83.4
median,85
A,2
B,1
C,1
D,1
F,0
"""

def main() -> None:
    """
    Main program execution
    """

    # Read student data
    students = read_students("data/students.csv")

    # Extract grades from CSV
    grades = [
        int(student["grade"])
        for student in students
    ]

    # Calculate statistics
    mean_grade = calculate_mean(grades)
    
    median_grade = calculate_median(grades)

    distribution = grade_distribution(grades)

    # Store results in one dict
    results = {
        "mean": mean_grade,
        "median": median_grade,
        "A": distribution["A"],
        "B": distribution["B"],
        "C": distribution["C"],
        "D": distribution["D"],
        "F": distribution["F"],
    }

    # Write results to CSV
    write_results("data/results.csv", results)

    print("Results written to results.csv")


if __name__ == "__main__":
    main()