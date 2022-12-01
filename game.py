class Game:

    def __init__(self, zmienna):
        self.zmienna = zmienna
        print('New Human was born!')

    def speak(self):
        print(f'I can speak and my name is {self.zmienna}!')


kuba = Game("Kuba")
kuba.speak()
