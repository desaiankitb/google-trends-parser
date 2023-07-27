import requests
from src.google_trends_parser import parse_google_trends_rss
from src.google_trends_to_mongodb import store_in_mongodb
from src.configutility import ConfigUtility

class SlackNotifier:
    """
    A utility class to send notifications to a Slack channel using a webhook URL.
    
    Attributes:
        webhook_url (str): The Slack webhook URL used to send notifications.
    """
    
    def __init__(self, webhook_url):
        """
        Initializes the SlackNotifier with the provided webhook URL.
        
        Args:
            webhook_url (str): The Slack webhook URL.
        """
        self.webhook_url = webhook_url

    def send_message(self, message):
        """
        Sends a message to the Slack channel associated with the webhook URL.
        
        Args:
            message (str): The message to be sent to the Slack channel.
            
        Returns:
            bool: True if the message was sent successfully, False otherwise.
        """
        payload = {"text": message}
        response = requests.post(self.webhook_url, json=payload)
        return response.status_code == 200

if __name__ == "__main__":
    """
    Main execution point. Parses the Google Trends RSS feed, extracts the trending data,
    stores it into a MongoDB collection, and sends a notification to Slack about the operation's status.
    """
    
    # Fetch Slack webhook URL using ConfigUtility
    config_util = ConfigUtility()
    slack_config = config_util.get_slack_config()
    webhook_url = slack_config['SLACK_WEBHOOK_URL']

    notifier = SlackNotifier(webhook_url)
    try:
        url = "https://trends.google.com/trends/trendingsearches/daily/rss?geo=US"
        trends = parse_google_trends_rss(url)
        store_in_mongodb(trends)
        notifier.send_message("Trends stored in MongoDB successfully!")
    except Exception as e:
        notifier.send_message(f"Error occurred: {str(e)}")