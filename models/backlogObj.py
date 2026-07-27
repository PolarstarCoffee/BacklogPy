import json
class backlogObj:
    def __init__(self, title="", description="", status="", thumbnail="", image_paths=None ):
        self.title = title
        self.description = description
        self.status = status
        self.thumbnail = thumbnail
        self.image_paths = image_paths or [thumbnail]