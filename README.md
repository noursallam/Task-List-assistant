# Task List Project

## Overview
This project is a task management system that allows users to add, view, and remove tasks. The project uses Python and the `pyttsx3` library for text-to-speech functionality, allowing the program to "speak" to the user when performing actions such as adding or removing tasks.

## Tools and Technologies Used

### 1. **Python**
   - Python is the core programming language for this project. It handles all the logic for managing tasks, saving/loading data, and interacting with the user via the terminal.

### 2. **pyttsx3**
   - **pyttsx3** is a Python library used for text-to-speech conversion. It allows the program to speak task details aloud, providing a more interactive experience.
   - It supports multiple voices (male/female) depending on the platform and settings.
   - Voice and speech rate can be customized using the `pyttsx3` engine.

### 3. **JSON (JavaScript Object Notation)**
   - Tasks are stored in a JSON file (`tasks.json`), which allows for easy saving and loading of tasks between program executions.
   - The `json` module in Python is used to handle reading and writing to the file.

### 4. **File System**
   - The program reads from and writes to a specified directory to store and retrieve the tasks. Make sure the directory exists and is accessible before running the program.
   - The task data is stored in `tasks.json` in the specified directory.

## Features

- **Add a task**: Allows the user to input a task and assign a priority.
- **View tasks**: Lists all tasks, sorted by their priority.
- **Remove a task**: Allows the user to remove a task by selecting it from the list.
- **Text-to-Speech**: The program speaks out task-related information, such as confirming actions or displaying task details.

## Getting Started

### Prerequisites
Make sure you have Python 3.x installed. You can download it from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/).

You also need to install the required libraries:

```bash
pip install pyttsx3
