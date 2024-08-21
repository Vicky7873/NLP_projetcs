from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml_file, create_directories
from textSummarizer.entity import DataIngestionConfig

# this peace of code is for the configuration manager where we will read the config/params yaml and and return the data to the entity folder, this will used in pipeline 
class ConfigurationManager:
    def __init__(self, config_filepath = CONFIG_FILE_PATH, params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml_file(config_filepath)
        self.params = read_yaml_file(params_filepath)
        # these 2 lines are for to read the path of config.yaml and params.yaml

        create_directories([self.config.artifacts_root])
        # this line of code is for to create the artifacts folder using the create_directories function from the common.py and using the DataIngestionConfig variables

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config