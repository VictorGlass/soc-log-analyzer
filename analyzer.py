# -------------------------------------
# SOC LOG ANALYZER - TIMESTAMP VERSION
# -------------------------------------

from datetime import datetime, timedelta
import os

# Dictionary to store failed login attempts
failed_attempts = {}


# Define time window for brute force detection
TIME_WINDOW = timedelta(minutes=5)

# Get current script directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build log file path
LOG_FILE = os.path.join(BASE_DIR, "sample_logs.txt")

print("====== SOC ANALYSIS REPORT ======\n")


# Open and read log file
with open(LOG_FILE, "r") as logs:


    # Process each line
    for line in logs:

        # Split log parts
        parts = line.strip().split()

        # Skip empty lines
        if len(parts) < 4:
            continue

        # Extract timestamp
        timestamp_str = parts[0] + " " + parts[1]

        # Convert timestamp into datetime object
        timestamp =datetime.strptime(
            timestamp_str,
            "%Y-%m-%d %H:%M:%S"
        )

        # Extract event type and IP
        event = parts[2]
        ip = parts[3]


        # 
        # FAILED LOGIN EVENTS
        #

        if event == "FAILED_LOGIN":

            # Create entry if IP doesn´t exist
            if ip not in failed_attempts:
                failed_attempts[ip] = []

            # Store failed attempt timestamp
            failed_attempts[ip].append(timestamp)

            print(f"[INFO] Failed login from {ip} at {timestamp}")

        #
        # SUCCESS LOGIN EVENTS
        #

        elif event == "SUCCESS_LOGIN":
            print(f"[INFO] Successul login from {ip} at {timestamp}")

    
#
# BRUTE FORCE ANALYSIS
#

print("\n====== BRUTE FORCE DETECTION ======\n")

# Analyze each IP
for ip, attempts in failed_attempts.items():

    # Sort timestamps
    attempts.sort()

    # Compare attempts
    for i in range(len(attempts)):

        count = 1

        for j in range(i + 1, len(attempts)):

            # Calculate difference
            difference = attempts[j] - attempts[i]

            # Check if attempts happened inside window
            if difference <= TIME_WINDOW:
                count += 1

        # Trigger alert if threshold reached
        if count >= 3:
            print(f"Possible brute force attack detected! ")
            print(f"IP Address: {ip}")
            print(f"Failed attempts: {count}")
            print(f"Detection window: 5 minutes\n")

            break

print("====== END OF REPORT ======")