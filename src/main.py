from src.extract import fetch_top_stories
from src.transform import transform_data
from src.load import load_data
import logging

def run_etl():
    logging.info("Starting ETL Pipeline...")
    
    raw_data = fetch_top_stories(limit=50)
    if not raw_data:
        logging.error("Extraction failed. Aborting pipeline.")
        return
        
    cleaned_data = transform_data(raw_data)
    load_data(cleaned_data)
    
    logging.info("ETL Pipeline completed successfully.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    run_etl()
