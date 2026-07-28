import storage.jsonStorage as jsonStorage
class backlogManager():
    #Here we define the backlogManager class, which will manage the backlog entries, the UI will never directly edit the backlog entries, 
    #it will always go through this class to do so. This is to ensure that the UI does not have direct access to the backlog entries, 
    #and that the backlog entries are always edited in a consistent manner.
    
    
    def __init__(self):
        self.entries = []
    def add(self, entry):
        self.entries.append(entry)
    def remove(self, entry):
        self.entries.remove(entry)
    def find(self, title):
        for entry in self.entries:
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
    def get_all(self):
        return self.entries
    def save_to_file(self, filename):
        storage = jsonStorage.jsonStorage()
        data = [entry.__dict__ for entry in self.entries]
        storage.save(data, filename)
    
    
    
             