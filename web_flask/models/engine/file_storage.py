#!/usr/bin/python3
"""
Update FileStorage: (models/engine/file_storage.py)
    Add a public method def close(self)::
		call reload() method for deserializing the JSON file to objects
"""


class FileStorage:
    """Class that serializes instances to a JSON file and deserializes JSON file to instances"""
    
    # Assuming you already have the following methods
    def reload(self):
        """Deserializes the JSON file to objects"""
        # Logic for deserializing the JSON file
        pass

    def close(self):
        """Public method that calls the reload() method"""
        self.reload()
