__all__ = [
    'story_data',
    'text_data',
    'zone_name',
    'text_index',
    'char_index',
    'zone_index'
]

import os
from typing import TypedDict, Any

from core.util import json
from core.constant import data_path, support_language


class StoryData(TypedDict):
    id: str
    type: str
    name: dict[support_language, str]
    zone: str


def get_path(filename: str):
    return os.path.join(data_path, 'story', filename + '.json')


def to_set(data: dict) -> dict[Any, set[Any]]:
    for k in data:
        data[k] = set(data[k])
    return data


story_data: dict[str, StoryData] = json.load(get_path('story_data'))
text_data: dict[str, dict[str, str]] = json.load(get_path('text_data'))
zone_name: dict[str, dict[support_language, str]] = json.load(get_path('zone_name'))
text_index: dict[str, set[str]] = to_set(json.load(get_path('text_index')))
char_index: dict[str, set[str]] = to_set(json.load(get_path('char_index')))
zone_index: dict[str, set[str]] = to_set(json.load(get_path('zone_index')))
