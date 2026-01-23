class backlogObj:
    def __init__(self, id, title, description, status):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.thumbnail = None  # Placeholder for thumbnail image
        self.rating = None    # Placeholder for rating
    def __repr__(self):
        return f"backlogObj(id={self.id}, title='{self.title}', description='{self.description}', status='{self.status}', thumbnail={self.thumbnail}, rating={self.rating})"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "thumbnail": self.thumbnail,
            "rating": self.rating
        }