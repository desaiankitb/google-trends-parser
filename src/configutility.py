import configparser

class ConfigUtility:
    def __init__(self, config_file='src/config.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get_mongo_config(self):
        return {
            'HOST': self.config.get('MONGODB', 'HOST', fallback='localhost'),
            'PORT': self.config.getint('MONGODB', 'PORT', fallback=27017),
            'USERNAME': self.config.get('MONGODB', 'USERNAME'),
            'PASSWORD': self.config.get('MONGODB', 'PASSWORD'),
            'DB_NAME': self.config.get('MONGODB', 'DB_NAME', fallback='ds_trends_db')
        }
