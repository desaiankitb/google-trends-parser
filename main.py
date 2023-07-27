from fastapi import FastAPI, BackgroundTasks
from src.google_trends_parser import parse_google_trends_rss
from src.google_trends_to_mongodb import store_in_mongodb
from src.configutility import ConfigUtility
from src.SlackNotifier import SlackNotifier

app = FastAPI()

def notify_slack(message):
    config_util = ConfigUtility()
    slack_config = config_util.get_slack_config()
    webhook_url = slack_config['SLACK_WEBHOOK_URL']
    notifier = SlackNotifier(webhook_url)
    notifier.send_message(message)

@app.get("/get_google_trends")
def get_google_trends(background_tasks: BackgroundTasks):
    try:
        url = "https://trends.google.com/trends/trendingsearches/daily/rss?geo=US"
        trends = parse_google_trends_rss(url)
        store_in_mongodb(trends)
        background_tasks.add_task(notify_slack, "Trends stored in MongoDB successfully!")
        return {"status": "success", "message": "Trends stored in MongoDB successfully!"}
    except Exception as e:
        background_tasks.add_task(notify_slack, f"Error occurred: {str(e)}")
        return {"status": "error", "message": f"Error occurred: {str(e)}"}