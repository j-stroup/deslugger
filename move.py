import tkinter as tk
from tkinter import simpledialog
import random
from datetime import datetime
import os
import winsound

# A list of realistic, 60-second desk resets
exercises = [
    "Stand up and stretch.",
    "Do a building lap",
    "Stretch your arms overhead and lean left/right for 30 seconds.",
    "Look at an object 20 feet away for 20 seconds (20-20-20 rule).",
    "Stand up, touch your toes, and take three deep breaths.",
    "Stand up and stretch your neck side to side."
]

def get_log_path():
    # Helper function to ensure we always point to the right file
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "water_log.txt")

def get_daily_total():
    log_file = get_log_path()
    today_date = datetime.now().strftime("%Y-%m-%d")
    total_ounces = 0
    
    # If the file exists, read it line by line
    if os.path.exists(log_file):
        with open(log_file, "r") as file:
            for line in file:
                # Only count lines that start with today's date
                if line.startswith(today_date):
                    try:
                        # Split the line at the hyphen and extract the number
                        # Example line: 2026-10-09 09:30 - 8 oz
                        oz_string = line.split(" - ")[1].replace(" oz", "").strip()
                        total_ounces += int(oz_string)
                    except (IndexError, ValueError):
                        pass # Skip any malformed lines without crashing
                        
    return total_ounces

def log_water(ounces):
    log_file = get_log_path()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    with open(log_file, "a") as file:
        file.write(f"{timestamp} - {ounces} oz\n")

def show_alert():
    # Initialize tkinter and hide the root window
    root = tk.Tk()
    root.withdraw()
    
    # Force the window to the top
    root.attributes("-topmost", True)
    
    # Trigger a subtle Windows 'ding' (the default Asterisk system sound)
    winsound.MessageBeep(winsound.MB_ICONASTERISK)
    
    # Calculate today's running total before building the prompt
    current_total = get_daily_total()
    task = random.choice(exercises)
    
    prompt_text = (f"Action: {task}\n\n"
                   f"Water total for today: {current_total} oz\n\n"
                   f"How many ounces of water are you drinking right now? (Enter 0 if none)")
    
    ounces = simpledialog.askinteger("Kinetic Reset & Hydration", prompt_text, parent=root, initialvalue=8, minvalue=0)
    
    if ounces is not None and ounces > 0:
        log_water(ounces)
        
    root.destroy()

if __name__ == "__main__":
    show_alert()