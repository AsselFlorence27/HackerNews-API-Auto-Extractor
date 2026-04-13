# HackerNews API Auto-Extractor

A Python pipeline that extracts trending stories from HackerNews and saves them to a local SQLite database.

## Overview
I built this project to automate data collection from HackerNews. It fetches the top stories, cleans the raw JSON responses, and updates the database tracking the stories over time.

## Architecture
- **Source**: HackerNews API (topstories)
- **Pipeline**: Python (`requests`)
- **Storage**: SQLite (`data.db`)
- **Automation**: GitHub Actions (Scheduled daily cron job)
- **Testing**: `pytest` unit testing suite (`tests/`)

## Setup and Usage

1. Create a virtual environment and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the test suite:
   ```bash
   python -m pytest tests/
   ```
3. Run the pipeline manually:
   ```bash
   python -m src.main
   ```
4. Query the results:
   ```bash
   sqlite3 data.db "SELECT * FROM top_stories LIMIT 5;"
   ```

## Workflow
The pipeline runs autonomously via GitHub Actions every day at 08:00 UTC. The CI/CD pipeline automatically runs the test suite before proceeding to extract and load data. The database file (`data.db`) is tracked and updated via git commits, ensuring a historical record of trending stories is maintained.
