thonfrom src.extractors.filters import apply_filters

def test_apply_filters_min_rating():
    tours = [
        {"price": 50, "rating": 4.5, "category": "Adventure"},
        {"price": 20, "rating": 3.0, "category": "Culinary"}
    ]
    filters = {"min_rating": 4.0}
    filtered = apply_filters(tours, filters)
    assert len(filtered) == 1
    assert filtered[0]["rating"] == 4.5