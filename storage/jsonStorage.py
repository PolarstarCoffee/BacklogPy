import json
import os

#save JSON file to data/JSON folder, if the folder does not exist, create it
class jsonStorage:
    def save(self, data, filename):
        desired_dir = "data/JSON"
        os.makedirs(desired_dir, exist_ok=True)
        with open(os.path.join(desired_dir, filename), 'w') as f:
            json.dump(data, f, indent=4)
    def load(self, filename):
        with open(filename, 'r') as f:
            return json.load(f)
    def delete(self, filename):
        import os
        if os.path.exists(filename):
            os.remove(filename)