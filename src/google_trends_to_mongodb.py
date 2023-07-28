from pymongo import MongoClient
from src.google_trends_parser import parse_google_trends_rss
from src.configutility import ConfigUtility
from src.logging_config import LoggerConfig

def store_in_mongodb(trends):
    """
    Stores the provided trends data into a MongoDB collection.
    
    Args:
        trends (list): A list of dictionaries containing trending data for each trend.
        
    Note:
        The MongoDB configuration is loaded from a 'config.ini' file using the ConfigUtility class.
    """
    
    logger = LoggerConfig().get_logger()
    logger.info("Starting the process to store trends in MongoDB.")
    
    # Load MongoDB configuration
    mongo_config = ConfigUtility().get_mongo_config()

    # Construct the connection string
    connection_string = f"mongodb://{mongo_config['USERNAME']}:{mongo_config['PASSWORD']}@{mongo_config['HOST']}:{mongo_config['PORT']}/{mongo_config['DB_NAME']}?authSource={mongo_config['DB_NAME']}"

    # Connect to the MongoDB server with the connection string
    client = MongoClient(connection_string)

    # Select the database and collection
    db = client[mongo_config['DB_NAME']]
    collection = db.ds_daily_trends

    # Insert each trend into the collection
    for trend in trends:
        collection.insert_one(trend)
        logger.debug(f"Inserted trend: {trend['title']} into MongoDB.")

    # Close the connection
    client.close()
    logger.info("Trends stored in MongoDB successfully.")


if __name__ == "__main__":
    """
    Main execution point. Parses the Google Trends RSS feed, extracts the trending data,
    and stores it into a MongoDB collection.
    """
    logger = LoggerConfig().get_logger()
    logger.info("Starting the main execution.")
    
    url = "https://trends.google.com/trends/trendingsearches/daily/rss?geo=US"
    trends = parse_google_trends_rss(url)
    store_in_mongodb(trends)
    print("Trends stored in MongoDB successfully!")
    logger.info("Main execution completed successfully.")