import storage.jsonStorage as jsonStorage
from models.backlogObj import backlogObj
from dataclasses import asdict
class backlogManager():
    def __init__(self):
        #where each entry is a backlogObj instance
        self._entries = []
        self._storage = jsonStorage.jsonStorage()
        
    def add(self, entry: backlogObj) -> None:
        self._entries.append(entry)
        
    def remove(self, entry: backlogObj):
        if isinstance(entry, str):
            self._entries = [e for e in self._entries if e.title != entry]
        else:
            self._entries = [e for e in self._entries if e != entry]

    def find(self, title: str) -> backlogObj | None:
        for entry in self._entries:
            if entry.title == title:
                return entry
        return None
    
    def edit(self, title, new_title=None, new_description=None, new_status=None, new_thumbnail=None, new_rating=None):
        entry = self.find(title)
        if entry:
            if new_title is not None:
                entry.title = new_title
            if new_description is not None:
                entry.description = new_description
            if new_status is not None:
                entry.status = new_status
            if new_thumbnail is not None:
                entry.thumbnail = new_thumbnail
            if new_rating is not None:
                entry.rating = new_rating
            return True
        return False
    
    def display_all_entries(self):
        return self._entries.copy()
    
    def save_to_file(self, filename):
        data = [asdict(entry) for entry in self._entries]
        self._storage.save(data, filename)

    def load_from_file(self, filename):
        data = self._storage.load(filename)
        self._entries = [backlogObj.backlogObj(**entry) for entry in data]
        
    def clear_entries(self):
        self._entries.clear()