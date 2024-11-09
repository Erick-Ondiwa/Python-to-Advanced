# multiple 2_inheritance: This is when a child class inherits from
# # more than one parent class
class Pray:
    pass


class Predator:
    def flee(self):
        print("This animal fleeing")


class Rabbit(Pray):
    def hunt(self):
        print("This animal hunting")


class Hawk(Predator):
    pass


class Fish(Pray, Predator):
    pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.hunt()
fish.flee()