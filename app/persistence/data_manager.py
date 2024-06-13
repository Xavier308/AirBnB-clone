import json
from .interface import IPersistenceManager

class DataManager(IPersistenceManager):
    def __init__(self, filename='mydata.json'):  # Default filename changed to 'mydata.json'
        self.filename = filename
        self.storage = self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}  # Return an empty dictionary if no data

    def save_to_file(self):
        with open(self.filename, 'w') as file:
            json.dump(self.storage, file, indent=4)

    # This "entity_id = entity.id" was changed to resolve problem
    def save(self, entity):
        entity_type = type(entity).__name__
        entity_id = entity.user_id  # Use user_id instead of id
        if entity_type not in self.storage:
            self.storage[entity_type] = {}
        self.storage[entity_type][entity_id] = entity.to_dict()
        self.save_to_file()

    def get(self, entity_id, entity_class):
        entity_type = entity_class.__name__
        entity_data = self.storage.get(entity_type, {}).get(str(entity_id), None)
        if entity_data:
            return entity_class(**entity_data)
        return None

    def update(self, entity):
        self.save(entity)  # Reuse save method since it handles replacing existing data

    def delete(self, entity_id, entity_class):
        entity_type = entity_class.__name__
        if entity_type in self.storage and entity_id in self.storage[entity_type]:
            del self.storage[entity_type][entity_id]
            self.save_to_file()
