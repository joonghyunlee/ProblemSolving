class Animal(object):
    pass


class Cat(Animal):
    def __repr__(self):
        return 'cat'


class Dog(Animal):
    def __repr__(self):
        return 'dog'


class AnimalShelter:
    def __init__(self):
        self.cats = []
        self.dogs = []
        self.order = 0

    def enqueue(self, animal):
        if isinstance(animal, Cat):
            self.cats.insert(0, (self.order, animal))
        elif isinstance(animal, Dog):
            self.dogs.insert(0, (self.order, animal))
        self.order += 1

    def dequeueAny(self):
        if not self.cats and not self.dogs:
            return None
        elif not self.cats:
            return self.dogs.pop()[1]
        elif not self.dogs:
            return self.cats.pop()[1]

        if self.cats[-1][0] > self.dogs[-1][0]:
            return self.dogs.pop()[1]
        return self.cats.pop()[1]

    def dequeueCat(self):
        if not self.cats:
            return None
        return self.cats.pop()[1]

    def dequeueDog(self):
        if not self.dogs:
            return None
        return self.dogs.pop()[1]


if __name__ == '__main__':
    s = AnimalShelter()
    s.enqueue(Cat())
    s.enqueue(Dog())
    s.enqueue(Dog())
    print s.dequeueAny()
    print s.dequeueCat()
    print s.dequeueAny()
    print s.dequeueDog()
    print s.dequeueDog()
