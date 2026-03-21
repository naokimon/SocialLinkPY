import json

class Player:
    def __init__(self, first_name, last_name, stats=None, current_day=1, current_time="day"):
        self.first_name = first_name
        self.last_name = last_name
        self.stats = stats if stats is not None else{
            "courage": 0,
            "diligence": 0,
            "understanding": 0,
            "expression": 0,
            "knowledge": 0,
        }
        self.current_day = current_day
        self.current_time = current_time

    @classmethod
    def from_save(cls, data):
        return cls(
            first_name=data.get("first_name", "Naoki"),
            last_name=data.get("last_name", "Mon"),
            stats=data.get("stats"),
            current_day=data.get("current_day", 1),
            current_time=data.get("current_time", "day")
        )