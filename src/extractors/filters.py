thondef apply_filters(tours, filters):
    if not filters:
        return tours

    def matches(tour):
        if "min_price" in filters and tour["price"] < filters["min_price"]:
            return False
        if "max_price" in filters and tour["price"] > filters["max_price"]:
            return False
        if "min_rating" in filters and tour["rating"] < filters["min_rating"]:
            return False
        if "category" in filters and tour["category"] != filters["category"]:
            return False
        return True

    return [t for t in tours if matches(t)]