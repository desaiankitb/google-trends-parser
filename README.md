# Google Trends to MongoDB with Slack Notifications and FastAPI

This project fetches daily trending searches from Google Trends, stores them in a MongoDB database, and sends notifications to a Slack channel regarding the status of the operation. Additionally, it exposes an API endpoint using FastAPI to trigger the fetching process.

## Prerequisites

- Python 3.x
- MongoDB server
- Slack webhook URL for notifications

## Installation

1. Clone the repository:

```bash
git clone <repository_url>
```

2. Navigate to the project directory:

```bash
cd google-trends-parser
```

3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Configuration

1. Update the `config.ini` file with the necessary MongoDB and Slack configurations:

```
[MONGODB]
HOST=localhost
PORT=27017
USERNAME=your_mongodb_username
PASSWORD=your_mongodb_password
DB_NAME=ds_trends_db

[SLACK]
SLACK_WEBHOOK_URL=your_slack_webhook_url
```

2. Ensure MongoDB is running and the provided user has the necessary permissions.

## Usage

To start the FastAPI server:

```bash
uvicorn main:app --reload
```

Navigate to `http://127.0.0.1:8000/get_google_trends` in your browser or use a tool like `curl` to access the endpoint. This will fetch the Google trends, store them in MongoDB, and send a Slack notification.

## Modules

### `src/google_trends_parser.py`

This module contains the `parse_google_trends_rss` function that fetches and parses the Google Trends RSS feed for daily trending searches.

### `store_in_mongodb`

This function connects to the MongoDB server using the provided configuration, selects the appropriate database and collection, and inserts the parsed trending searches.

### `SlackNotifier`

A utility class to send notifications to a Slack channel:

- `__init__(self, webhook_url)`: Initializes the SlackNotifier with the provided webhook URL.
- `send_message(self, message)`: Sends a message to the Slack channel associated with the webhook URL.

\## Notifications

The application sends notifications to a Slack channel using the provided webhook URL. Notifications are sent when:

- The trending searches are successfully stored in MongoDB.
- An error occurs during the operation.
