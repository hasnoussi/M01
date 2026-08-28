#!/usr/bin/env python3
# class = notre plan (tamplate = modele) de notre "object" => est une instance d'une calss
class Plant:
    def __init__(self, name, height, age): # self = variable qui pointe vers l'objet sur lequel en travalle. c'est une référance (pointeur sof qu'ici on manipules jamais l'adresse mémoire directement, python gére ca automatiquement) mais le comportement est identique
        self.name = name # => paramètre( disparaît après cette etape) VS self.name => attribut (presante dans l'objet)
        self.height = height
        self.age = age
    
    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old") # la logique d'affichage est edantique, fait une seule fois,en cas de changement de format, c'est facile a modifier
        #la classe s'arrête ici
print("=== Garden Plant Registry ===") # rien avoir avec notre class, il est indepondant, on peut meme le mettre tous au debut avant de declarer notre class
if __name__ == "__main__":
    # ici on crée des instances = "object" chaque plant est stocke dans une variable séparée ex: p1, p2, p3 
    p1 = Plant("Rose", 25, 30) # chaque plante est indepondante, on evite de melanger les attreibuts
    p2 = Plant("Sunflower", 80, 45)
    p3 = Plant("Cactus", 15, 120)
    

    p1.show() #  sans  le  show() = print(f"{p1.name => (attribut = une donnée portée par un object)}: {p1.height}cm, {p1.age} days old")
    # liée directement a l'objet, pas de risque d'appler la fonction avec les mauvais paramètre
    p2.show() # "Méthode" = un comportement portée par l'objet
    p3.show()
    # stocker nombre ilimité de plant(instance) dans simple liste
