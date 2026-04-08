import asyncio


def clean_data(data):
    """Remove None values and strip strings."""
    if not isinstance(data, list):
        raise TypeError("Input must be a list")

    cleaned = []
    for item in data:
        if item is None:
            continue
        if isinstance(item, str):
            item = item.strip()
        cleaned.append(item)

    return cleaned


def normalize_numbers(numbers):
    """Normalize numbers between 0 and 1."""
    if not numbers:
        return []

    min_val = min(numbers)
    max_val = max(numbers)

    if min_val == max_val:
        return [0.0 for _ in numbers]

    return [(x - min_val) / (max_val - min_val) for x in numbers]


def process_user_data(users):
    """Extract usernames in lowercase."""
    result = []
    for user in users:
        if "name" not in user:
            raise KeyError("Missing name")
        result.append(user["name"].lower())
    return result


def fetch_data():
    """Simulates an external API call."""
    return [" real data "]


def get_cleaned_data():
    data = fetch_data()
    return clean_data(data)


async def async_fetch():
    await asyncio.sleep(0.1)
    return [1, 2, 3]