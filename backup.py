# Import the necessary libraries
import os  # Provides functions to interact with the operating system
import shutil  # Offers high-level file operations, like copying
import datetime  # For handling date and time
import schedule  # For scheduling scripts to run at a particular time
import time  # For time-related tasks

# Define the source and destination directories
source_dir = "C:/Users/sabuh/OneDrive/Desktop/Prefecture/ID"  # Path to the folder you want to copy
destination_dir = "C:/Users/sabuh/OneDrive/Desktop/BackUps"  # Path to the folder where the copy should go

def copy_folder_to_directory(source, dest):
    # Function to copy a folder to a specified directory with the current date as the folder name
    
    today = datetime.date.today()  # Get the current date
    dest_dir = os.path.join(dest, str(today))  # Create a new destination path with the current date
    
    try:
        shutil.copytree(source, dest_dir)  # Try to copy the entire folder tree to the new destination
        print(f"Folder copied to: {dest_dir}")  # Success message
    except FileExistsError:
        # If a folder with today's date already exists at the destination
        print(f"Folder already exists in: {dest}")  # Print an error message

# Schedule the folder copy operation
# Set the script to call the `copy_folder_to_directory` function every day at 13:59 (1:59 PM)
schedule.every().day.at("13:59").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

while True:
    # Keep the script running and check for any scheduled tasks
    schedule.run_pending()  # Check if a scheduled task is due to run
    time.sleep(60)  # Wait for 60 seconds before checking again
