# Import necessary modules
import os
import sys
import logging

# Define the logging format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"

# Define the directory for log files
log_dir = "logs"

# Define the filepath for the log file
log_filepath = os.path.join(log_dir, "running_logs.log")

# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Configure logging settings
logging.basicConfig(
    level=logging.INFO,  # Set logging level to INFO
    format=logging_str,  # Set logging format
    handlers=[
        logging.FileHandler(log_filepath),  # Write log messages to file
        logging.StreamHandler(sys.stdout)  # Display log messages on the console
    ]
)

# Get the logger object
logger = logging.getLogger("mlProjectLogger")

# Log a message to confirm that logging is configured successfully
logger.info("Logging is configured successfully!")
