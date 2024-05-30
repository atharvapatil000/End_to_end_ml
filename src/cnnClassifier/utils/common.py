## Utils are used when we want to use few function frequently

import os  # Importing the 'os' module for interacting with the operating system.
from box.exceptions import BoxValueError  # Importing a specific exception class from the 'box.exceptions' module.
import yaml  # Importing the 'yaml' module for working with YAML files.
from .. import logger  # Importing the 'logger' object from the 'cnnClassifier' module.
import json  # Importing the 'json' module for working with JSON data.
import joblib  # Importing the 'joblib' module for working with binary data.
from ensure import ensure_annotations  # Importing a decorator for ensuring type annotations in function signatures.
from box import ConfigBox  # Importing a class called 'ConfigBox' from the 'box' module.
from pathlib import Path  # Importing the 'Path' class from the 'pathlib' module for working with file paths.
from typing import Any  # Importing a type hint for 'Any' type.
import base64  # Importing the 'base64' module for encoding and decoding binary data.

# Defining a function to read YAML files and return a ConfigBox object.
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:  # Starting a try block to handle exceptions.
        with open(path_to_yaml) as yaml_file:  # Opening the YAML file.
            content = yaml.safe_load(yaml_file)  # Loading the content of the YAML file safely.
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")  # Logging a message indicating successful loading of the YAML file.
            return ConfigBox(content)  # Returning the content of the YAML file as a ConfigBox object.
    except BoxValueError:  # Handling a specific type of exception related to BoxValueError.
        raise ValueError("yaml file is empty")  # Raising a ValueError if the YAML file is empty.
    except Exception as e:  # Handling any other type of exception.
        raise e  # Reraising the exception.

# Defining a function to create directories specified in the input list.
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:  # Iterating through each path in the list.
        os.makedirs(path, exist_ok=True)  # Creating the directory if it doesn't exist.
        if verbose:  # Checking if verbose mode is enabled.
            logger.info(f"created directory at: {path}")  # Logging a message indicating the creation of the directory.

# Defining a function to save JSON data to a file.
@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:  # Opening the JSON file in write mode.
        json.dump(data, f, indent=4)  # Writing the JSON data to the file with indentation.

    logger.info(f"json file saved at: {path}")  # Logging a message indicating successful saving of the JSON file.

# Defining a function to load JSON data from a file.
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:  # Opening the JSON file.
        content = json.load(f)  # Loading the JSON data from the file.

    logger.info(f"json file loaded succesfully from: {path}")  # Logging a message indicating successful loading of the JSON file.
    return ConfigBox(content)  # Returning the content as a ConfigBox object.

# Defining a function to save binary data to a file.
@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)  # Saving the binary data to the file using joblib.

    logger.info(f"binary file saved at: {path}")  # Logging a message indicating successful saving of the binary file.

# Defining a function to load binary data from a file.
@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)  # Loading the binary data from the file using joblib.

    logger.info(f"binary file loaded from: {path}")  # Logging a message indicating successful loading of the binary file.
    return data  # Returning the loaded data.

# Defining a function to get the size of a file in KB.
@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)  # Calculating the size of the file in KB.
    return f"~ {size_in_kb} KB"  # Returning the size as a string.

# Defining a function to decode Base64 encoded image data and save it to a file.
def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)  # Decoding the Base64 encoded image data.
    with open(fileName, 'wb') as f:  # Opening the file in binary write mode.
        f.write(imgdata)  # Writing the decoded image data to the file.

# Defining a function to encode an image file into Base64 format.
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:  # Opening the image file in binary read mode.
        return base64.b64encode(f.read())  # Encoding the image data into Base64 format and returning it.
