thonimport random
from datetime import datetime, timedelta
from utils.logger import get_logger

logger = get_logger(__name__)

class ReviewParser:
    def __init__(self, http_client):
        self.http = http_client

    def fetch_reviews(self, tour_url: str, limit: int = 5):
        logger.info(f"Fetching reviews for {tour_url}")
        reviews = []
        for i in range(limit):
            reviews.append({
                "review_text": f"Review {i+1} for {tour_url}",
                "review_rating": random.randint(3, 5),
                "review_date": (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d")
            })
        return reviews