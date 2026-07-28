from dataclasses import dataclass, field
import json
@dataclass
class backlogObj:
    title: str = ""
    description: str = ""
    status: str = ""
    thumbnail: str = ""
    image_paths: list = field(default_factory=list)