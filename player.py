import json

class Player:
    instance = None
    def __init__(self, first_name, last_name, current_location, level=1, stats=None, current_day=1, current_time="day"):
        self.first_name = first_name
        self.last_name = last_name
        self.current_location = current_location
        self.level = level
        self.stats = stats if stats is not None else{
            "courage": 0,
            "diligence": 0,
            "understanding": 0,
            "expression": 0,
            "knowledge": 0,
        }
        self.current_day = current_day
        self.current_time = current_time
        Player.instance = self

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def from_save(cls, data):
        return cls(
            first_name=data.get("first_name", "Yu"),
            last_name=data.get("last_name", "Narukami"),
            current_location=data.get("current_location", "bedroom"),
            level=data.get("level", 1),
            stats=data.get("stats"),
            current_day=data.get("current_day", 1),
            current_time=data.get("current_time", "Afternoon")
        )

    def to_save(self):
        return {
            "player": {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "full_name": self.full_name,
                "current_location": self.current_location,
                "level": self.level,
                "stats": self.stats,
                "current_day": self.current_day,
                "current_time": self.current_time
            }
        }