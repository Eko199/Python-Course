def validate(category: str, time_window: str, format: str) -> bool:
    valid: bool = True

    if category not in ["tv", "movie", "all"]:
        print(f"Invalid category {category}! Should be tv/movie/all.")
        valid = False

    if time_window not in ["day", "week"]:
        print(f"Invalid time window {time_window}! Should be day/week.")
        valid = False

    if format not in ["json", "csv"]:
        print(f"Invalid time window {format}! Should be json/csv.")
        valid = False

    return valid