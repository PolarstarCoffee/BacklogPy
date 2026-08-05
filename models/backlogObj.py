from dataclasses import dataclass, field
import json
from PIL import Image
@dataclass
class backlogObj:
    title: str = ""
    description: str = ""
    status: str = ""
    #be sure the thumbnail and image types are correct
    thumbnail: str = ""
    image_paths: list = field(default_factory=list)
    
    
#validate paths for thumbnail and images
def post_init__(self):
    if not isinstance(self.image_paths, list):
        raise ValueError("image_paths must be a list")
    for path in self.image_paths:
        if not isinstance(path, str):
            raise ValueError("Each image path must be a string")
backlogEntry = backlogObj("Sample Title", "Sample Description", "In Progress", "path/to/thumbnail.jpg", ["path/to/image1.jpg", "path/to/image2.jpg"])
print(backlogEntry)