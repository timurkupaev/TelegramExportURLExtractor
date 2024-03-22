# TelegramExportURLExtractor

TelegramExportURLExtractor is a Python application designed to extract URLs from JSON files exported from Telegram chat history. It provides a simple GUI to load individual JSON files or entire folders (including subfolders), extract URLs from chat messages, and save the extracted URLs to a text file.

## Features

- Process single or multiple JSON files exported from Telegram.
- Process folders. Recursively search through directories to find JSON files.
- Extract URLs from the chat history contained within JSON files.
- Display and Save the extracted URLs to a text file.


## Usage

1. **Load JSON Files**: Click the "Load JSON Files" button to select individual JSON files.
2. **Load Folder with JSON Files**: Click the "Load Folder with JSON Files" button to select a directory. The application will automatically find all JSON files within the selected directory and its subdirectories.
3. **Save URLs to File**: After URLs have been extracted and displayed, click the "Save URLs to File" button to save them to a text file. You will be prompted to choose a location and filename.
