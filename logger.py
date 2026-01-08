import csv, os
from datetime import datetime

os.makedirs("logs", exist_ok=True)

def log(file, row):
    with open(f"logs/{file}", "a", newline="") as f:
        csv.writer(f).writerow([datetime.now()] + row)
