class Character:
    """Represents NON-COMBAT data about a game entity"""

    def __init__(self, age, race_template):
        self.race_name = race_template["race_name"]
        self.race_description = race_template["race_description"]
        self.age = age
