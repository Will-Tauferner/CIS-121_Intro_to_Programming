class Dog:
    def __init__(self,breed,color,personality):
        self.breed = breed 
        self.color = color
        self.personality = personality

        def get_name(self):
            return self.breed
        def get_color(self):
            return self.color
        def get_personality(self):
            return self.personality
        def set_breed(self,new_breed):
            self.breed = new_breed


lab = Dog('yellow lab','yellow','friendly')
pitbull = Dog('pitbull','grey', 'aggressive')

class DogPark:
    def __init__(self, _name):
        self.name = _name
        self.dogs = []
    def add_dog(self,dog):
        self.dogs.append(dog):
    def show_dogs(self):
        for dog in self.dogs:
            print(dog.get_name())
    def change_dog_name(self,old_name, new_name):
        for dog in self.dogs:
            if dog.get_name() == old_name:
                dog.set_name(new_name)
    def find_dog(self, dog_name):
        for dog in self.dogs:
            if dog.get_name() == old_name:
                dog.speak()
    def call_dog(self, dog_name):
        '''This calls the dog and removes it from the park'''
    


park1 = DogPark('Bark Zone')

park1.add_dog('Rover', 3, 'Mastiff')
park1.add_dog('spot', 2, 'lab')

park1.show_dogs()
park1.change_dog_name('spoot', 'spot')
park1.show_dogs()
park1.call_dog('Rover')
park1.show_dogs()



