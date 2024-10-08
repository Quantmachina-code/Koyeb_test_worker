import time

def perform_task():
    print("Performing background task...")

if __name__ == "__main__":
    while True:
        perform_task()
        time.sleep(10)  # Wait for 10 seconds before repeating the task
