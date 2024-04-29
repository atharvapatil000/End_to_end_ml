# Import necessary libraries
import os  # Importing the os library to interact with the operating system
from pathlib import Path  # Importing Path from pathlib to handle system paths
import logging  # Importing logging to enable logging of messages for debugging

# Configuring the logging to display info level messages and include the time of the log message
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Define the name of the project
project_name = "mlProject"

# List of file paths to be created for the project setup
list_of_files = [
    ".github/workflows/.gitkeep",  # GitHub Actions workflow folder
    f"src/{project_name}/__init__.py",  # Init file for making Python packages
    f"src/{project_name}/components/__init__.py",  # Init file for components package
    f"src/{project_name}/utils/__init__.py",  # Init file for utils package
    f"src/{project_name}/utils/common.py",  # Common utilities
    f"src/{project_name}/config/__init__.py",  # Init file for config package
    f"src/{project_name}/config/configuration.py",  # Configuration settings
    f"src/{project_name}/pipeline/__init__.py",  # Init file for pipeline package
    f"src/{project_name}/entity/__init__.py",  # Init file for entity package
    f"src/{project_name}/entity/config_entity.py",  # Config entities
    f"src/{project_name}/constants/__init__.py",  # Init file for constants package
    "config/config.yaml",  # YAML configuration file
    "params.yaml",  # YAML parameters file
    "schema.yaml",  # YAML schema definition file
    "main.py",  # Main Python script
    "app.py",  # Python script for app
    "Dockerfile",  # Dockerfile for containerization
    "requirements.txt",  # File listing dependencies
    "setup.py",  # Setup script for package distribution
    "research/trials.ipynb",  # Jupyter notebook for research and trials
    "templates/index.html",  # HTML template for the web application
    "test.py"  # Script for running tests
]

# Iterate through each file path in the list to create directories and files
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert the filepath string to a Path object for easier manipulation
    filedir, filename = os.path.split(filepath)  # Split the filepath into directory and file name

    # Check if the directory exists and create it if not
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Create the directory if it does not exist; no error if existing
        logging.info(f"Creating directory; {filedir} for the file: {filename}")  # Log the creation of the directory

    # Create the file if it does not exist or if it's empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:  # Open the file in write mode to create it
            pass  # Pass statement is a placeholder; it does nothing
        logging.info(f"Creating empty file: {filepath}")  # Log the creation of the file

    # Log a message if the file already exists and is not empty
    else:
        logging.info(f"{filename} is already exists")  # Log that the file already exists
