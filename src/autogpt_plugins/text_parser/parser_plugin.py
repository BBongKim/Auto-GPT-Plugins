import os
from .parsers import parser_map

def parse_text(filename: str) -> str:
    """
    Parse text from file and return the results as a string.
    """
    file_extension = os.path.splitext(filename)[1].lower()
    parser = parser_map.get(file_extension)
    return parser.parse(filename)