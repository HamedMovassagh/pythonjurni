class animal:
    alive=True

    def eat(self):
        print("this animal can eat")
    def sleep(self):
        print("this animal can sleep")    
class Rabitt(animal):
    def run(self):
        print("this rabbit can run")
class Fish(animal):
    def swim(self):
        print("this fish can swim")
class Hawke(animal):
    def fly(self):
        print("this Hawek can fly")      


rabitt=Rabitt()
rabitt.eat()        
