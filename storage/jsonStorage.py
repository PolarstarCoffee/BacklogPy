import json
import os


class jsonStorage:
    def save(self, data, filename):
        desired_dir = "<c>:/dev/backlogApp/data"
        full_path = os.path.join(desired_dir, filename)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    def load(self, filename):
        with open(filename, 'r') as f:
            return json.load(f)
    def delete(self, filename):
        import os
        if os.path.exists(filename):
            os.remove(filename)