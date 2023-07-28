import logging
import sys

class LoggerConfig:
    def __init__(self, name=__name__, level=logging.INFO):
        self.logger = logging.getLogger(name)
        if not self.logger.hasHandlers():  # Check if handlers already exist
            self.setup(level)

    def setup(self, level):
        self.logger.setLevel(level)
        
        # Formatter
        formatter = logging.Formatter('[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s')

        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger
