import ctypes
import time

def display_toast_notification(title, message):
    # Load the Windows library
    ctypes.windll.user32.MessageBoxW(0, message, title, 0)

def main():
    while True:
        # Display the toast notification
        display_toast_notification("Reminder", "Drink some water!")
        # Wait for an hour
        time.sleep(3600)

if __name__ == "__main__":
    main()