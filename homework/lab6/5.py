class Animal:
    def __init__(self, name, teritory, python=False):
        self.name = name
        self.teritory = teritory
        self.python = python

    def get_teritory(self):
        return self.teritory
    
    def is_python(self):
        return 'Python > Java' if self.python else 'still Python > Java'
    
    def make_sound(self):
        return 'I am an animal'
    
class Mammal(Animal):
    def __init__(self, name, teritory, fur_color, is_python=False):
        super().__init__(teritory, name, is_python)
        self.fur_color = fur_color

    def get_fur_color(self):
        return self.fur_color
    
    def make_sound(self):
        return 'Moo'
    
class Bird(Animal):
    def __init__(self, name, teritory, wing_span, is_python=False):
        super().__init__(teritory, name, is_python)
        self.feather_color = wing_span

    def get_feather_color(self):
        return self.feather_color

    def make_sound(self):
        return 'Chirp chirp se apropie licenta'
    
class Fish(Animal):
    def __init__(self, name, teritory, water_type, is_python=False):
        super().__init__(teritory, name, is_python)
        self.water_type = water_type

    def get_water_type(self):
        return self.water_type
    
    def make_sound(self):
        return 'Blub blub'
    
animals = [Mammal('Cow', 'Farm', 'Brown'), Bird('Sparrow', 'City', 'Brown'), Fish('Goldfish', 'Aquarium', 'Fresh'), Animal('Python', 'Jungle', True)]
for animal in animals:
    if isinstance(animal, Mammal):
        print(animal.get_fur_color())
    elif isinstance(animal, Bird):
        print(animal.get_feather_color())
    elif isinstance(animal, Fish):
        print(animal.get_water_type())
    print(animal.make_sound())
    print(animal.is_python())
    print()
