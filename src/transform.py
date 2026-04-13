import datetime
import logging

def clean_story(item_data):
    """Transform raw API response into a standardized dictionary."""
    return {
        "id": item_data.get("id"),
        "title": item_data.get("title", "No Title"),
        "url": item_data.get("url", ""),
        "score": item_data.get("score", 0),
        "author": item_data.get("by", "Unknown"),
        "retrieved_at": datetime.datetime.now(datetime.timezone.utc).isoformat()
    }

def transform_data(raw_stories):
    logging.info(f"Transforming {len(raw_stories)} raw stories.")
    cleaned_data = [clean_story(item) for item in raw_stories if item.get("id")]
    logging.info(f"Successfully transformed {len(cleaned_data)} stories.")
    return cleaned_data
