import csv
import json
import os

# Get the current directory of the Python script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Specify the relative path to the JSON file in the "data" directory
json_file = os.path.join(current_directory, "..", "data", "data.json")


# Read the JSON data from the file
with open(json_file, "r") as json_file:
    data = json.load(json_file)

# Specify the CSV file name
csv_file = "output.csv"

# Define the CSV field names
field_names = [
    "id",
    "active",
    "title",
    "summary",
    # Add other field names here
]

# Open the CSV file for writing
with open(csv_file, mode="w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=field_names)

    # Write the header row
    writer.writeheader()

    # Write the data from the JSON to the CSV file
    for item in data:
        writer.writerow(item)

print(f"Data from {json_file} has been successfully converted to {csv_file}")
