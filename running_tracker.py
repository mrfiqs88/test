import time
import math
import csv
from datetime import datetime

# Function to calculate distance (in km) using steps and stride length
def calculate_distance(steps, stride_length_m=0.78):
    # stride length default = 0.78m (average adult)
    distance_m = steps * stride_length_m
    return distance_m / 1000  # convert to kilometers

# Function to calculate average speed
def calculate_speed(distance_km, duration_sec):
    if duration_sec == 0:
        return 0
    return distance_km / (duration_sec / 3600)  # km/h

# Main tracker class
class RunningTracker:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.steps = 0

    def start_run(self):
        input("Press ENTER to start your run...")
        self.start_time = time.time()
        print("🏃 Run started! Type 'stop' to finish.")
        while True:
            cmd = input("Type 'step' to log a step or 'stop' to finish: ").lower()
            if cmd == "step":
                self.steps += 1
            elif cmd == "stop":
                self.end_run()
                break
            else:
                print("Invalid input, use 'step' or 'stop'.")

    def end_run(self):
        self.end_time = time.time()
        duration = self.end_time - self.start_time
        distance_km = calculate_distance(self.steps)
        speed_kmh = calculate_speed(distance_km, duration)

        print("\n✅ Run Summary:")
        print(f"🕒 Duration: {duration:.2f} seconds")
        print(f"🚶 Steps: {self.steps}")
        print(f"📏 Distance: {distance_km:.3f} km")
        print(f"⚡ Avg Speed: {speed_kmh:.2f} km/h")

        self.save_run(duration, distance_km, speed_kmh)
        print("\nRun saved to runs.csv!")

    def save_run(self, duration, distance, speed):
        filename = "runs.csv"
        fieldnames = ["date", "duration_sec", "steps", "distance_km", "avg_speed_kmh"]

        # Create file with headers if it doesn't exist
        try:
            with open(filename, 'x', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
        except FileExistsError:
            pass

        # Save run data
        with open(filename, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "duration_sec": round(duration, 2),
                "steps": self.steps,
                "distance_km": round(distance, 3),
                "avg_speed_kmh": round(speed, 2)
            })

# Run the tracker
if __name__ == "__main__":
    tracker = RunningTracker()
    tracker.start_run()
