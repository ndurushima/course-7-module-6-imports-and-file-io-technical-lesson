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
    """Search the log file for lines that match a keyword."""
    # TODO: Try opening the log file for reading
    # TODO: Read each line and filter for lines that include the keyword (case insensitive)
    # TODO: Print matched log lines or a 'not found' message
    # TODO: Handle FileNotFoundError gracefully
    pass