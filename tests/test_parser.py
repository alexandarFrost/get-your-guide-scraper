thonimport json
from src.extractors.tour_parser import TourParser
from src.extractors.review_parser import ReviewParser
from src.utils.http_client import HttpClient

def test_tour_parser_generates_data():
    http = HttpClient()
    parser = TourParser(http)
    tours = parser.fetch_tours("test", limit=3)
    assert len(tours) == 3
    assert all("tour_title" in t for t in tours)

def test_review_parser_returns_reviews():
    http = HttpClient()
    parser = ReviewParser(http)
    reviews = parser.fetch_reviews("https://example.com", limit=2)
    assert len(reviews) == 2
    assert "review_text" in reviews[0]