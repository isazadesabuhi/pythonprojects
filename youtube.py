# Import the YouTube class from the pytube library for downloading videos
from pytube import YouTube
# Import tkinter for GUI operations and filedialog for directory selection dialogs
import tkinter as tk
from tkinter import filedialog

# Define the download_video function that takes a video URL and save path as input
def download_video(url, save_path):
    try:
        # Create a YouTube object with the provided URL
        yt = YouTube(url)
        # Filter the video streams to only progressive mp4 streams
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        # Get the highest resolution stream available
        highest_res_stream = streams.get_highest_resolution()
        # Download the video to the specified save path
        highest_res_stream.download(output_path=save_path)
        # Print success message
        print("Video downloaded successfully!")
    except Exception as e:
        # Print any errors that occur during the download process
        print(e)

# Define the open_file_dialog function to open a dialog for directory selection
def open_file_dialog():
    # Open the directory selection dialog
    folder = filedialog.askdirectory()
    # If a folder is selected, print its path
    if folder:
        print(f"Selected folder: {folder}")
    # Return the selected folder path
    return folder

# Main execution block, only runs if the script is executed as the main program
if __name__ == "__main__":
    # Initialize the tkinter GUI environment
    root = tk.Tk()
    # Hide the main tkinter window as it's not needed
    root.withdraw()
    
    # Prompt the user to enter a YouTube URL
    video_url = input("Please enter a Youtube url: ")
    # Open the file dialog for the user to select a save directory
    save_dir = open_file_dialog()
    
    # Check if a save directory was selected
    if save_dir:
        # Print a message indicating the download has started
        print("Started download....")
        # Call the download_video function with the URL and save directory
        download_video(video_url, save_dir)
    else:
        # Print a message if no valid save location was selected
        print("Invalid save location")