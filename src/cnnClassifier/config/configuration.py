from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from src.cnnClassifier.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    """
    ConfigurationManager is responsible for managing configuration and parameter files for the CNN Classifier.
    It reads the configuration from YAML files and sets up the necessary directories.
    """

    def __init__(self, config_filepath: str = CONFIG_FILE_PATH, params_filepath: str = PARAMS_FILE_PATH):
        """
        Initialize the ConfigurationManager with the provided configuration and parameters file paths.
        Reads the YAML files and sets up the artifact root directory.

        :param config_filepath: Path to the configuration YAML file
        :param params_filepath: Path to the parameters YAML file
        """
        try:
            # Read configuration and parameters from YAML files
            self.config = read_yaml(config_filepath)
            self.params = read_yaml(params_filepath)

            # Create the artifact root directory specified in the configuration
            create_directories([self.config['artifacts_root']])
        except Exception as e:
            # Raise a ValueError if there is an issue with initialization
            raise ValueError(f"Error initializing ConfigurationManager: {e}")

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Get the data ingestion configuration from the loaded YAML configuration.
        Sets up the necessary directories for data ingestion.

        :return: DataIngestionConfig object with data ingestion configuration
        """
        try:
            # Access data ingestion configuration from the loaded config
            config = self.config['data_ingestion']

            # Create the root directory for data ingestion specified in the config
            create_directories([config['root_dir']])
            
            # Create a DataIngestionConfig object with the required properties
            data_ingestion_config = DataIngestionConfig(
                root_dir=config['root_dir'],
                source_URL=config['source_URL'],
                local_data_file=config['local_data_file'],
                unzip_dir=config['unzip_dir']
            )
            
            # Return the DataIngestionConfig object
            return data_ingestion_config
        except KeyError as e:
            # Raise a KeyError if a required key is missing in the configuration
            raise KeyError(f"Missing required configuration key: {e}")
        except Exception as e:
            # Raise a ValueError if there is any other issue with getting the data ingestion config
            raise ValueError(f"Error getting data ingestion config: {e}")
