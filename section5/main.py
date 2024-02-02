class Car():
    def __init__(self, model) -> None:
        self.model = model
    def run(self):
        print('run')

class Toyota(Car):
    def run(self):
        print('fast')




