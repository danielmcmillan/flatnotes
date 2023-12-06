import os
import re
import shutil
from typing import List, Tuple


def strip_ext(filename):
    return os.path.splitext(filename)[0]


def camel_case(snake_case_str: str) -> str:
    """Return the declared snake_case string in camelCase."""
    parts = [part for part in snake_case_str.split("_") if part != ""]
    return parts[0] + "".join(part.title() for part in parts[1:])


def empty_dir(path):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)


def re_extract(pattern, string) -> Tuple[str, List[str]]:
    """Similar to re.sub but returns a tuple of:

    - `string` with matches removed
    - list of matches"""
    matches = []
    text = re.sub(pattern, lambda tag: matches.append(tag.group()), string)
    return (text, matches)


def is_valid_filename(filename):
    r"""Return False if the declared filename contains any of the following
    characters: <>:"\|?*, or if any path segment is empty, '.', or '..'."""
    invalid_chars = r'<>:"\|?*'
    if any(invalid_char in filename for invalid_char in invalid_chars):
        return False

    for segment in filename.split('/'):
        if segment in ['', '.', '..']:
            return False

    return True
