"""
running_tracker.py
A simple command-line running tracker that logs runs to a CSV file.
"""

import csv
from datetime import datetime

FILE_NAME = "runs.csv"

def log_run(distance_km, time_minutes):
    """Logs a run to the CSV file."""
    pace = time_minutes / distance_km  # minutes per km
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([now, distance_km, time_minutes, round(pace, 2)])

    print(f"✅ Run logged: {distance_km} km in {time_minutes} min (pace: {round(pace, 2)} min/km)")

def view_runs():
    """Displays all logged runs."""
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            print("\n📊 Your Running Log:")
            print("-" * 40)
            for row in reader:
                print(f"Date: {row[0]}, Distance: {row[1]} km, Time: {row[2]} min, Pace: {row[3]} min/km")
    except FileNotFoundError:
        print("⚠️ No runs logged yet!")

def main():
    print("🏃 Running Tracker 🏃")
    print("1. Log a new run")
    print("2. View run history")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        distance = float(input("Enter distance (km): "))
        time = float(input("Enter time (minutes): "))
        log_run(distance, time)
    elif choice == "2":
        view_runs()
    else:
        print("Goodbye!")

if __name__ == "__main__":
    main()
