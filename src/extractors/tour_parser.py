thonimport json
import random
from utils.logger import get_logger

logger = get_logger(__name__)

class TourParser:
    def __init__(self, http_client):
        self.http = http_client

    def fetch_tours(self, query: str, limit: int = 10):
        logger.info(f"Simulating fetch for tours: {query}")
        # Simulated data for demonstration
        tours = []
        for i in range(limit):
            tours.append({
                "tour_id": str(500000 + i),
                "tour_title": f"Tour {i+1} for {query}",
                "location": "Jakarta, Indonesia",
                "category": random.choice(["Adventure", "Sightseeing", "Culinary"]),
                "price": round(random.uniform(20, 200), 2),
                "currency": "USD",
                "rating": round(random.uniform(3.5, 5.0), 1),
                "total_reviews": random.randint(20, 500),
                "description": "A great tour experience.",
                "url": f"https://www.getyourguide.com/tour-{500000 + i}"
            })
        return tours