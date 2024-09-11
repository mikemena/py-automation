import os
import csv

# Keywords for equipment and muscles
equipment_keywords = [
    "band",
    "banded",
    "barbell",
    "cable",
    "dumbbell",
    "ez-bar",
    "kettlebell",
    "smith-machine",
]
muscle_keywords = ["tricep", "chest", "bicep", "back", "shoulder", "leg", "ab", "core"]


def detect_equipment(filename):
    """
    Detects equipment based on keywords in the filename.
    Returns the equipment type if found, otherwise an empty string.
    """
    for equipment in equipment_keywords:
        if equipment in filename.lower():
            return equipment
    return ""


def detect_muscle(filename):
    """
    Detects muscle group based on keywords in the filename.
    Returns the muscle group if found, otherwise an empty string.
    """
    for muscle in muscle_keywords:
        if muscle in filename.lower():
            return muscle
    return ""


def write_to_csv(folder_path, output_csv):
    """
    Goes through the folder, collects GIF filenames, and writes the results into a CSV file.

    Args:
        folder_path (str): Path to the folder with GIFs.
        output_csv (str): Path to the output CSV file.
    """
    with open(output_csv, mode="w", newline="") as file:
        writer = csv.writer(file)
        # Write headers
        writer.writerow(["Filename", "Equipment", "Muscle"])

        # Loop through the folder and process each file
        for filename in os.listdir(folder_path):
            if filename.endswith(".gif"):
                equipment = detect_equipment(filename)
                muscle = detect_muscle(filename)
                # Write the data to the CSV
                writer.writerow([filename, equipment, muscle])

    print(f"Data written to {output_csv} successfully.")


# Specify the folder containing the GIFs and the output CSV file
gif_folder = os.path.expanduser("~/exercise-gifs")
output_file = os.path.expanduser("~/exercise-gifs/_gif_data.csv")

# Run the function to create the CSV
write_to_csv(gif_folder, output_file)
