class Character:
    def __init__(self, race, age):
        self.race = race
        self.age = age

        if self.race:
            self.race.owner = self
