class Dog:

    scientific_name = "Canis lupus familiaris"

    def __init__(self, name):
        self.name = name
        self.woofs = 0

    def speak(self):
        print("Woof!")

    def hear(self, words):
        if self.name in words:
            self.speak()

    def count(self):
        self.woofs += 1
        for bark in range(self.woofs):
            self.speak()

class Huski(Dog):
    origin = "Siberia"

    def speak(self):
        print("Woooooof")

class Cat:

    def __init__(self):
        self.mood = "neutral"

    def speak(self):
        if self.mood == "happy":
            print("Purrr")
        elif self.mood == "angry":
            print("Hiss!")
        else:
            print("Meow!")