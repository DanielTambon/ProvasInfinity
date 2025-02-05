class Animal:
    def falar(self):
        print("Este animal faz um som.")

class Cachorro(Animal):
    def falar(self):
        print("O cachorro late.")

class Gato(Animal):
    def falar(self):
        print("O gato mia.")

# Testando as classes
animal = Animal()
animal.falar()  # Saída: Este animal faz um som.

dog = Cachorro()
dog.falar()  # Saída: O cachorro late.

cat = Gato()
cat.falar()  # Saída: O gato mia.
