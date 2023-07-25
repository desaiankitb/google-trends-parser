# Google Trends Daily Scraper

This script fetches the daily trending searches from Google Trends for the current and previous day.

## Prerequisites

- Python 3.x

## Setup

1. **Clone this repository.**
```   
git clone https://github.com/desaiankitb/google-trends-parser.git
```

2. **Navigate to the repository's directory.**
```
cd <repository-directory>
```

3. **Install the required packages.**
```
pip install -r requirements.txt
```

## Usage

Run the script using the following command:
```
python google_trends_scraper.py
```

This will print the trending searches for the current and previous day in the console.

## Output

The script outputs a list of dictionaries. Each dictionary represents a trend and contains the following keys:
- `title`: The title of the trend.
- `ht:approx_traffic`: Approximate traffic for the trend.
- `description`: Description of the trend.
- `link`: Link to the trend on Google Trends.
- `pubDate`: Publication date of the trend.
- `ht:picture`: Link to the picture associated with the trend.
- `ht:picture_source`: Source of the picture.
- `news_items`: A list of news items associated with the trend. Each news item is a dictionary containing the title, snippet, URL, and source.

## License

This project is open source and available under the [MIT License](LICENSE).
