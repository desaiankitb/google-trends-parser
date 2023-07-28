import configparser
from src.logging_config import LoggerConfig

class ConfigUtility:
    """
    Utility class to manage configurations from a given configuration file.
    
    Attributes:
        config (ConfigParser): An instance of ConfigParser to read the configuration file.
        logger (Logger): Logger instance for logging.
    """
    
    def __init__(self, config_file='src/config.ini'):
        """
        Initializes the ConfigUtility with a given configuration file.
        
        Args:
            config_file (str): Path to the configuration file. Defaults to 'src/config.ini'.
        """
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        
        # Initialize logger
        self.logger = LoggerConfig().get_logger()
        self.logger.info(f"ConfigUtility initialized with config file: {config_file}")

    def get_mongo_config(self):
        """
        Fetches the MongoDB configuration from the configuration file.
        
        Returns:
            dict: A dictionary containing MongoDB configurations such as HOST, PORT, USERNAME, PASSWORD, and DB_NAME.
        """
        self.logger.info("Fetching MongoDB configuration from config file.")
        return {
            'HOST': self.config.get('MONGODB', 'HOST', fallback='localhost'),
            'PORT': self.config.getint('MONGODB', 'PORT', fallback=27017),
            'USERNAME': self.config.get('MONGODB', 'USERNAME'),
            'PASSWORD': self.config.get('MONGODB', 'PASSWORD'),
            'DB_NAME': self.config.get('MONGODB', 'DB_NAME', fallback='ds_trends_db')
        }
    
    def get_slack_config(self):
        """
        Fetches the Slack configuration from the configuration file.
        
        Returns:
            dict: A dictionary containing the Slack webhook URL.
        """
        self.logger.info("Fetching Slack configuration from config file.")
        return {
            'SLACK_WEBHOOK_URL': self.config.get('SLACK', 'SLACK_WEBHOOK_URL')
        }
