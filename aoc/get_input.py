import requests
from pathlib import Path


CACHE = Path(__file__).parent / "cache"


def get_input(day: int, year: int):
    YEAR_CACHE = CACHE / str(year)
    YEAR_CACHE.mkdir(parents=True, exist_ok=True)
    cookie_file = CACHE / "cookie2.txt"
    day_file = YEAR_CACHE / f"day{day}.txt"
    if day_file.exists():
        with open(day_file) as f:
            return f.read()

    with open(cookie_file) as f:
        headers = {"Cookie": f.read()}

    r = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", headers=headers)

    with open(day_file, "w") as f:
        f.write(r.text)

    return r.text



