import uuid
from datetime import datetime

class City:
    def __init__(self, name, country, created_at=None, updated_at=None):
        self.city_id = str(uuid.uuid4())
        self.name = name
        self.country = country  # This should be a Country object or a reference
        self.created_at = self.parse_datetime(created_at)
        self.updated_at = self.parse_datetime(updated_at)

    def to_dict(self):
        return {
            "city_id": self.city_id,
            "name": self.name,
            "country": self.country.to_dict() if self.country else None,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

    @staticmethod
    def parse_datetime(date_str):
        if date_str:
            return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')
        else:
            return datetime.now()

    def __eq__(self, other):
        if not isinstance(other, City):
            return NotImplemented
        return (self.name == other.name and
                self.country == other.country)
