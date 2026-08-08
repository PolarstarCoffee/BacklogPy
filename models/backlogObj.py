from dataclasses import dataclass, field
import json
from PIL import Image
@dataclass
class backlogObj:
    title: str = ""
    description: str = ""
    status: str = ""
    #be sure the thumbnail and image types are correct
    thumbnail: Image = field(default=None)
    general_image: Image = field(default=None)
    image_paths: list = field(default_factory=list)
    
    
#validate paths for thumbnail and images
def post_init__(self):
    if not isinstance(self.title, str):
        raise ValueError("title must be a string")
    if not isinstance(self.thumbnail, Image.Image):
        raise ValueError("thumbnail must be a PIL Image object")
    if not isinstance(self.image_paths, list):
        raise ValueError("image_paths must be a list")
    for path in self.image_paths:
        if not isinstance(path, str):
            raise ValueError("Each image path must be a string")


#might need to look at converting the image to a different format for 
#storage or transmission
#in addition to converting the dataclass object to a dictionary or JSON 

