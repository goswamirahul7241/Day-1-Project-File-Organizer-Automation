**File Organizer Automation - Implementation Plan**

Goal Description
Create a Python script that automatically organizes files in a specified directory into subfolders based on their file extensions (Images, Videos, Documents, Music, ZIP, Others).

NOTE
The script will move files. It is recommended to test on a copy of data first.

Proposed Changes
File Organizer Script

[NEW] 
organizer.py
Inputs: Folder path (via command line argument or user input).
Logic:
Define a dictionary mapping extensions to folder names.
Iterate through files in the given directory.
Skip directories.
Determine the destination folder based on extension.
Create the destination folder if it doesn't exist.
Move the file.

Mappings:
Images: .jpg, .jpeg, .png, .gif, .bmp, .svg, .webp
Videos: .mp4, .mkv, .flv, .avi, .mov, .wmv
Documents: .pdf, .docx, .doc, .txt, .xlsx, .xls, .pptx, .ppt, .csv
Music: .mp3, .wav, .aac, .flac
ZIP: .zip, .rar, .7z, .tar, .gz
Others: Everything else

Verification Plan

Automated Tests

Create a temporary directory with dummy files of various types.
Run organizer.py on that directory.
Assert that files are moved to the correct subfolders.
Clean up the temporary directory.

Manual Verification
Run the script on a test folder created by the user (or me) and visually inspect the results.
Clean up the temporary directory.
Manual Verification
Run the script on a test folder created by the user (or me) and visually inspect the results.   
