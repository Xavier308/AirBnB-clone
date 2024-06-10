from .interface import IPersistenceManager


class DataManager(IPersistenceManager):
    def __init__(self):
        self.storage = {}

    def save(self, entity):
        entity_type = type(entity).__name__
        entity_id = entity.id
        if entity_type not in self.storage:
            self.storage[entity_type] = {}
        self.storage[entity_type][entity_id] = entity

    def get(self, entity_id, entity_type):
        return self.storage.get(entity_type, {}).get(entity_id, None)

    def update(self, entity):
        entity_type = type(entity).__name__
        entity_id = entity.id
        if entity_type in self.storage and entity_id in self.storage[entity_type]:
            self.storage[entity_type][entity_id] = entity

    def delete(self, entity_id, entity_type):
        if entity_type in self.storage and entity_id in self.storage[entity_type]:
            del self.storage[entity_type][entity_id]
