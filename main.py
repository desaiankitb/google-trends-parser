from src.google_trends_parser import parse_google_trends_rss
from src.google_trends_to_mongodb import store_in_mongodb
from src.configutility import ConfigUtility
from src.SlackNotifier import SlackNotifier


if __name__ == "__main__":
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
