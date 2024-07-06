class Oven:
    def __init__(self, temperature, time):
        self.temperature = temperature
        self.time = time

    def __str__(self):
        return f"Temperature: {self.temperature}°C, Time: {self.time} minutes"

    def to_dict(self):
        return {
            'temperature': self.temperature,
            'time': self.time
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['temperature'], data['time'])
