import os
import zipfile
import gdown
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    """
    DataIngestion class handles downloading and extracting data required for the CNN Classifier.
    """

    def __init__(self, config: DataIngestionConfig):
        """
        Initialize the DataIngestion with a given configuration.

        :param config: An instance of DataIngestionConfig containing configuration settings.
        """
        self.config = config

    def download_file(self) -> str:
        """
        Download the dataset from the specified URL in the configuration.
        
        :return: The path to the downloaded file.
        """
        try:
            dataset_url = self.config.source_URL  # URL to download the dataset from
            zip_download_dir = self.config.local_data_file  # Local path to save the downloaded zip file
            
            # Ensure the directory for data ingestion artifacts exists
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            
            # Log the start of the download process
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            # Extract the file ID from the Google Drive URL
            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            
            # Download the file using gdown
            gdown.download(prefix + file_id, zip_download_dir)
            
            # Log the successful download
            logger.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")

        except Exception as e:
            # Raise any exceptions encountered during the download process
            raise e

    def extract_zip_file(self):
        """
        Extract the downloaded zip file into the specified directory.

        :return: None
        """
        try:
            unzip_path = self.config.unzip_dir  # Directory to extract the zip file into
            
            # Ensure the directory for extracted data exists
            os.makedirs(unzip_path, exist_ok=True)
            
            # Extract the zip file using zipfile module
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
                
            # Log the successful extraction
            logger.info(f"Extracted zip file {self.config.local_data_file} into directory {unzip_path}")

        except Exception as e:
            # Raise any exceptions encountered during the extraction process
            raise e