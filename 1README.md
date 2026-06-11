# Smart File Organizer Using Python

## Project Overview

Smart File Organizer is a Python automation project that automatically organizes files into separate folders based on their file extensions. It helps users keep their directories clean and well-structured by reducing manual file management efforts.

## Objective

The objective of this project is to automate file organization by:

- Identifying file types using extensions
- Creating folders automatically
- Moving files into appropriate folders
- Maintaining operation logs
- Handling errors efficiently

## Features

- Automatic file sorting
- Organizes files by extension
- Creates folders dynamically
- User-defined folder selection
- Error handling using try-except
- Operation logging
- Simple command-line interface

## Technologies Used

- Python
- OS Module
- Shutil Module
- Logging Module

## Requirements

No external libraries are required.

Python Version:

```bash
Python 3.x
```

## Project Structure

```text
Smart_File_Organizer
│
├── organizer.py
├── operations.log
├── README.md
```

## How It Works

1. User enters a folder path.
2. Program scans all files in the folder.
3. File extensions are identified.
4. Separate folders are created automatically.
5. Files are moved into corresponding folders.
6. Operations are recorded in a log file.

## Example

### Before Organization

```text
Downloads/
│
├── photo.jpg
├── notes.pdf
├── video.mp4
├── image.png
```

### After Organization

```text
Downloads/
│
├── JPG/
│   └── photo.jpg
│
├── PDF/
│   └── notes.pdf
│
├── MP4/
│   └── video.mp4
│
├── PNG/
│   └── image.png
```

## How to Run

Open terminal in the project folder and execute:

```bash
python organizer.py
```

Enter the folder path when prompted.

Example:

```text
Enter Folder Path:
D:\Downloads
```

## Sample Output

```text
========== SMART FILE ORGANIZER ==========

Enter Folder Path:
D:\Downloads

Files Organized Successfully!
```

## Learning Outcomes

- File handling in Python
- Directory management using OS module
- Automation scripting
- Exception handling
- Logging implementation
- User input processing

## Future Enhancements

- GUI using Tkinter
- Duplicate file detection
- File size analysis
- Automatic scheduled organization

