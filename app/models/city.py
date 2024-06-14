import uuid
from datetime import datetime

class City:
    def __init__(self, name, country_code, created_at=None, updated_at=None, **kwargs):
        self.id = str(uuid.uuid4())  # Change 'city_id' to 'id' to standardize the identifier across all entities
        self.name = name
        self.country_code = country_code
        self.user_id = str(uuid.uuid4()) #added to debugg
        self.created_at = self.parse_datetime(created_at) if created_at else datetime.now()
        self.updated_at = self.parse_datetime(updated_at) if updated_at else datetime.now()

        # Use the ID from kwargs if it's provided, otherwise generate a new one.
        if 'id' in kwargs:
            self.id = kwargs['id']

    def to_dict(self):
        """Converts the city object to a dictionary for easier serialization."""
        return {
            "id": self.id,  # Change here as well to reflect the standardized 'id'
            "name": self.name,
            "country_code": self.country_code, # debugg
            "user_id": self.user_id, 
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

    @staticmethod
    def parse_datetime(date_str):
        """Parse a datetime string into a datetime object if present, including milliseconds."""
        if date_str:
            # Updated format to handle milliseconds
            try:
                return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')
            except ValueError:
                # Fallback for strings without milliseconds
                return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')
        else:
            return datetime.now()


    def __eq__(self, other):
        """Check equality based on name and country_code."""
        if not isinstance(other, City):
            return NotImplemented
        return self.id == other.id
