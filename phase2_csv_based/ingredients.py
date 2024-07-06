class Ingredients:
    def __init__(self, dough, sauce=None, toppings=None):
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings if toppings else []

    def __str__(self):
        return f"Dough: {self.dough}, Sauce: {self.sauce}, Toppings: {', '.join(self.toppings)}"

    def to_dict(self):
        return {
            'dough': self.dough,
            'sauce': self.sauce,
            'toppings': self.toppings
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['dough'], data.get('sauce'), data.get('toppings', []))
