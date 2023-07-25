import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

def parse_google_trends_rss(url):
    response = requests.get(url)
    root = ET.fromstring(response.content)

    # Define the namespace
    ns = {'ht': 'https://trends.google.com/trends/trendingsearches/daily'}

    # Extract global metadata
    global_meta_data = {
        'title': root.find('channel/title').text,
        'description': root.find('channel/description').text,
        'link': root.find('channel/link').text
    }

    # Get today's and yesterday's date in IST
    today_ist = datetime.now().strftime('%a, %d %b %Y')
    yesterday_ist = (datetime.now() - timedelta(days=1)).strftime('%a, %d %b %Y')

    trends = []

    for item in root.findall('channel/item', ns):
        pubDate = item.find('pubDate').text
        pubDate_ist = datetime.strptime(pubDate, '%a, %d %b %Y %H:%M:%S %z').strftime('%a, %d %b %Y')

        # Process items from yesterday or today (IST)
        if pubDate_ist == today_ist or pubDate_ist == yesterday_ist:
            trend_data = {
                'global_meta_data': global_meta_data,
                'title': item.find('title').text,
                'ht:approx_traffic': item.find('ht:approx_traffic', ns).text if item.find('ht:approx_traffic', ns) is not None else None,
                'description': item.find('description').text,
                'link': item.find('link').text,
                'pubDate': pubDate,
                'ht:picture': item.find('ht:picture', ns).text if item.find('ht:picture', ns) is not None else None,
                'ht:picture_source': item.find('ht:picture_source', ns).text if item.find('ht:picture_source', ns) is not None else None,
                'news_items': []
            }

            # Extract news items associated with the trend
            for news_item in item.findall('ht:news_item', ns):
                news_data = {
                    'ht:news_item_title': news_item.find('ht:news_item_title', ns).text,
                    'ht:news_item_snippet': news_item.find('ht:news_item_snippet', ns).text,
                    'ht:news_item_url': news_item.find('ht:news_item_url', ns).text,
                    'ht:news_item_source': news_item.find('ht:news_item_source', ns).text
                }
                trend_data['news_items'].append(news_data)

            trends.append(trend_data)

    return trends

if __name__ == "__main__":
    url = "https://trends.google.com/trends/trendingsearches/daily/rss?geo=US"
    trends = parse_google_trends_rss(url)
    for trend in trends:
        print(trend)