import requests
import logging

TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL_TEMPLATE = "https://hacker-news.firebaseio.com/v0/item/{}.json"

def fetch_top_stories(limit=50):
    logging.info(f"Fetching top {limit} stories from HackerNews API.")
    try:
        response = requests.get(TOP_STORIES_URL)
        response.raise_for_status()
        story_ids = response.json()[:limit]
        
        raw_stories = []
        for story_id in story_ids:
            item_response = requests.get(ITEM_URL_TEMPLATE.format(story_id))
            if item_response.status_code == 200:
                raw_stories.append(item_response.json())
                
        logging.info(f"Successfully extracted {len(raw_stories)} stories.")
        return raw_stories
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data from API: {e}")
        return []
