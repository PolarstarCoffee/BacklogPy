import storage.jsonStorage as jsonStorage
import models.backlogObj as backlogObj
class backlogManager():
    def __init__(self):
        self._entries = []
        
    def add(self, entry):
        self._entries.append(entry)
        
    def remove(self, entry):
        if isinstance(entry, str):
            self._entries = [e for e in self._entries if e.title != entry]
        else:
            self._entries = [e for e in self._entries if e != entry]

    def find(self, title):
        for entry in self._entries:
            if entry.title == title:
                return entry.copy()
            
    
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
        return [entry.copy() for entry in self._entries]
    
    def save_to_file(self, filename):
        storage = jsonStorage.jsonStorage()
        data = [entry.__dict__ for entry in self._entries]
        storage.save(data, filename)