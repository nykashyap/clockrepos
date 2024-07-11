import time
from datetime import datetime

def set_alarm(alarm_time):
    # Convert the alarm time to a datetime object
    alarm_time = datetime.strptime(alarm_time, "%H:%M:%S").time()
    print(f"Alarm set for {alarm_time}")

    while True:
        # Get the current time
        current_time = datetime.now().time()

        # Check if the current time matches the alarm time
        if current_time >= alarm_time:
            print("Wake up! It's time!")
            break

        # Wait for 1 second before checking the time again
        time.sleep(1)

# Example usage
alarm_time = input("Enter the alarm time (HH:MM:SS): ")
set_alarm(alarm_time)
