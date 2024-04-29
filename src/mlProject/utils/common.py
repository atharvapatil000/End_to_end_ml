import os  # Import the os module to interact with the operating system
from box.exceptions import BoxValueError  # Import specific exception for handling Box errors
import yaml  # Import the yaml module to handle YAML files
from .. import logger
import json  # Import the json module for JSON file manipulation
import joblib  # Import the joblib module for saving and loading binary files
from ensure import ensure_annotations  # Import the ensure_annotations decorator to enforce type checks
from box import ConfigBox  # Import ConfigBox from box, a dictionary that allows attribute-style access
from pathlib import Path  # Import the Path class from pathlib for filesystem paths
from typing import Any  # Import Any from typing for type annotations where any type is acceptable

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """ Function to read a YAML file and return its contents as a ConfigBox.
        path_to_yaml (Path): The filesystem path to the YAML file.
        Raises ValueError if the YAML file is empty, and re-raises any other exception encountered.
        Returns the contents of the YAML file as a ConfigBox, which allows attribute-style access.
    """
    try:
        with open(path_to_yaml) as yaml_file:  # Open the file at path_to_yaml for reading
            content = yaml.safe_load(yaml_file)  # Load the content of the file safely as a Python dict
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")  # Log the successful loading
            return ConfigBox(content)  # Convert the dict to ConfigBox and return it
    except BoxValueError:
        raise ValueError("yaml file is empty")  # Handle and raise a new ValueError if the YAML file is empty
    except Exception as e:
        raise e  # Re-raise any other exceptions encountered

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """ Function to create directories.
        path_to_directories (list): A list of paths where directories should be created.
        verbose (bool, optional): If True, logs the creation of directories.
        Iterates over each path in the list and creates directories at those paths.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)  # Create the directory at path; no error if it already exists
        if verbose:
            logger.info(f"created directory at: {path}")  # Log the directory creation if verbose is True

@ensure_annotations
def save_json(path: Path, data: dict):
    """ Function to save a dictionary to a JSON file.
        path (Path): The path to the JSON file where data should be saved.
        data (dict): The dictionary to save in JSON format.
        Saves the dictionary to a file at the specified path in JSON format with an indentation of 4 spaces.
    """
    with open(path, "w") as f:  # Open the file at path for writing
        json.dump(data, f, indent=4)  # Dump the data to the file as JSON
    logger.info(f"json file saved at: {path}")  # Log the successful save

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """ Function to load data from a JSON file and return as a ConfigBox.
        path (Path): The path to the JSON file.
        Returns the loaded data as a ConfigBox for attribute-style access.
    """
    with open(path) as f:  # Open the file at path for reading
        content = json.load(f)  # Load the content of the file as a Python dict
    logger.info(f"json file loaded succesfully from: {path}")  # Log the successful loading
    return ConfigBox(content)  # Convert the dict to ConfigBox and return it

@ensure_annotations
def save_bin(data: Any, path: Path):
    """ Function to save arbitrary data to a binary file using joblib.
        data (Any): The data to save.
        path (Path): The path to the binary file.
        Uses joblib to serialize and save data to the file.
    """
    joblib.dump(value=data, filename=path)  # Serialize and save the data to the file at path
    logger.info(f"binary file saved at: {path}")  # Log the successful save

@ensure_annotations
def load_bin(path: Path) -> Any:
    """ Function to load data from a binary file.
        path (Path): The path to the binary file.
        Returns the deserialized data from the file.
    """
    data = joblib.load(path)  # Deserialize and load the data from the file at path
    logger.info(f"binary file loaded from: {path}")  # Log the successful loading
    return data  # Return the loaded data

@ensure_annotations
def get_size(path: Path) -> str:
    """ Function to get the size of a file in kilobytes.
        path (Path): The path to the file.
        Returns the size of the file in kilobytes as a formatted string.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)  # Get the file size in bytes, convert to kilobytes, and round it
    return f"~ {size_in_kb} KB"  # Return the size formatted as a string with "KB"