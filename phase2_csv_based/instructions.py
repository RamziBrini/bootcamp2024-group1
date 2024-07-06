class Instructions:
    def __init__(self, preparation, cooking):
        self.preparation = preparation
        self.cooking = cooking

    def __str__(self):
        return f"Preparation: {self.preparation}, Cooking: {self.cooking}"

    def to_dict(self):
        return {
            'preparation': self.preparation,
            'cooking': self.cooking
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['preparation'], data['cooking'])
