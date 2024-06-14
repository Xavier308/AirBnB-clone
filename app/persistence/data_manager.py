import json
import os
from .interface import IPersistenceManager
from app.models.user import User
from app.models.city import City
from app.models.country import Country
from app.models.amenity import Amenity
from app.models.review import Review
from app.models.place import Place


class DataManager(IPersistenceManager):
    def __init__(self):
        self.files = {
            'User': 'userdata.json',
            'City': 'citydata.json',
            'Country': 'countrydata.json',
            'Amenity': 'amenitydata.json',
            'Review': 'reviewdata.json',
            'Place': 'placedata.json'
        }
        self.entity_classes = {
            'User': User,
            'City': City,
            'Country': Country,
            'Amenity': Amenity,
            'Review': Review,
            'Place': Place
        }
        self.storages = {key: self.load_data(key) for key in self.files}

    def load_data(self, entity_type):
        file_path = self.files[entity_type]
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                json.dump({}, file)
            return {}
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError, PermissionError) as e:
            print(f"Error loading data from {file_path}: {e}")
            return {}

    def save_to_file(self, entity_type):
        with open(self.files[entity_type], 'w') as file:
            json.dump(self.storages[entity_type], file, indent=4)

    def save(self, entity):
        entity_type = type(entity).__name__
        entity_id = entity.user_id
        if entity_type not in self.storages:
            self.storages[entity_type] = {}
        self.storages[entity_type][entity_id] = entity.to_dict()
        self.save_to_file(entity_type)

    def get(self, entity_id, entity_type):
        entity_data = self.storages.get(entity_type, {}).get(str(entity_id), None)
        if entity_data:
            entity_class = self.entity_classes.get(entity_type)
            if not entity_class:
                raise ValueError(f"No class found for entity type {entity_type}")
            return entity_class(**entity_data)
        return None

    def update(self, entity):
        self.save(entity)

    def delete(self, entity_id, entity_class):
        entity_type = entity_class.__name__
        if entity_type in self.storages and entity_id in self.storages[entity_type]:
            del self.storages[entity_type][entity_id]
            self.save_to_file(entity_type)

    def get_all(self, entity_type):
        return list(self.storages.get(entity_type, {}).values())
