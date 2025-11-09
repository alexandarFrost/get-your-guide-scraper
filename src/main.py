thonimport json
from pathlib import Path
from extractors.tour_parser import TourParser
from extractors.review_parser import ReviewParser
from extractors.filters import apply_filters
from utils.http_client import HttpClient
from utils.logger import get_logger

logger = get_logger(__name__)

def load_settings():
    config_path = Path(__file__).parent / "config" / "settings.json"
    with open(config_path, "r") as f:
        return json.load(f)

def main():
    settings = load_settings()
    http = HttpClient(proxy=settings.get("proxy"))
    tour_parser = TourParser(http)
    review_parser = ReviewParser(http)

    query = settings.get("query", "Jakarta day trips")
    limit = settings.get("limit", 10)
    filters = settings.get("filters", {})

    logger.info(f"Fetching tours for query: {query}")
    tours = tour_parser.fetch_tours(query, limit)
    filtered_tours = apply_filters(tours, filters)

    logger.info(f"Found {len(filtered_tours)} tours after filtering. Extracting reviews...")
    for tour in filtered_tours:
        tour["reviews"] = review_parser.fetch_reviews(tour["url"], limit=5)

    output_path = Path(__file__).resolve().parents[1] / "data" / "sample_output.json"
    with open(output_path, "w") as f:
        json.dump(filtered_tours, f, indent=2)

    logger.info(f"Data saved to {output_path}")

if __name__ == "__main__":
    main()