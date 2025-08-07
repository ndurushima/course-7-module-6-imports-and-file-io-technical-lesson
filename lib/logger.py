from datetime import datetime
import os

LOG_PATH = "data/user_logs.txt"

def log_action(action, log_file=LOG_PATH):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, 'a') as file:
        file.write(f"{timestamp} - {action}\n")

log_action("User logged in")
log_action("User updated profile")

def search_logs(keyword, log_file=LOG_PATH):
    try:
        with open("user_logs.txt", "r") as file:
            for line in file:
                if keyword in line:
                    print(line.strip())
    except FileNotFoundError:
        print("Log file not found")

search_logs("profile")