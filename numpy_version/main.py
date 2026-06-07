import csv
import numpy as np

"""
Grade Calculator (NumPy Version)

Reads student grades from a CSV file,
calculates statistics using NumPy,
and writes results to a CSV file.
"""

def read_grades(filename: str) -> np.ndarray:
    """Read grades from a CSV file and return them as a NumPy array"""

    # Open the CSV file for reading
    with open(filename, newline="") as file:
        reader = csv.DictReader(file) # read the CSV file into dicts

        # Extract the "grade" column and convert each value to an integer
        grades = np.array(
            [int(row["grade"]) for row in reader]
        )

    return grades



def write_results(
        filename: str,
        results: dict[str, float | int]
) -> None:
    """Write calculated statistics to a CSV file"""

    # Open the output file in write mode
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(["metric", "value"])

        # Write all metric-value pairs from the dictionary
        writer.writerows(results.items())

    

def main() -> None:

    # Load grades from the input CSV file
    grades = read_grades("data/students.csv")

    # Calculate statistics and grade distributions using NumPy
    results = {
        "mean": np.mean(grades),            # Average grade
        "median": np.median(grades),        # Middle grade
        "std": np.std(grades),              # Standard deviation
        "min": np.min(grades),              # Lowest grade
        "max": np.max(grades),              # Highest grade

        # Count grades in each letter-grade range
        "A": np.sum(grades >= 90),
        "B": np.sum((grades >= 80) & (grades < 90)),
        "C": np.sum((grades >= 70) & (grades < 80)),
        "D": np.sum((grades >= 60) & (grades < 70)),
        "F": np.sum((grades < 60)),

        # Percentage of students who passed (grade >= 60)
        "pass_rate": np.mean(grades >= 60) * 100,
    }

    # Save results to a CSV file
    write_results("data/results.csv", results)

    print("Results written successfully")

if __name__ == "__main__":
    # Run the program only when this file is executed directly
    main()
