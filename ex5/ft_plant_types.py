#!/usr/bin/env python3
class Plant:
    def __init__(self, name, height, age_d):
        self.name = name 
        self._height = height
        self._age_d = age_d
    
    def grow(self):
        self._height = round(self._height + 0.8, 1)
    def age(self):
        self._age_d = self._age_d + 1
    def show(self):
        print(f"{self.name}: {self._height}cm, {self._age_d} days old")
    def  track_week(self):
        self.show()
        height_debut = self._height
        for i in range(7):
            print(f"=== Day {i + 1} ===")
            self.age()
            self.grow()
            self.show()
        croissance = round(self._height - height_debut, 1)
        print(f"Growth this week: {croissance}cm")
    
    def set_height(self, nouvelle_valeur):
        if nouvelle_valeur >= 0:
            self._height = nouvelle_valeur
            print(f"Height updated: {self._height:.0f}cm")
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
    def set_age(self, nouvelle_valeur): 
        if nouvelle_valeur >= 0:
            self._age_d = nouvelle_valeur
            print(f"Age updated: {nouvelle_valeur} days")
            print()
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            print()
    def get_height(self):
        return self._height
    def get_age(self):
        return self._age_d

class Flower(Plant):
    def __init__(self, name, height, age_d, color):
        super().__init__(name, height, age_d)
        self.color = color
        self.bloomed = False
    def show(self):
        super().show()
        print(f" Color: {self.color}")
        if self.bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")    
    def bloom(self):
        self.bloomed = True
class Tree (Plant):
    def __init__(self, name, height, age_d, trunk_diameter):
        super().__init__(name, height, age_d)
        self.trunk_diameter = trunk_diameter
    
    def show(self):
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")
    def produce_shade(self):
        print(f"Tree {self.name} now produces a shade of {self._height}cm long and {self.trunk_diameter} wide.")
        

class Vegetable (Plant):
    def __init__(self, name, height, age_d, harvest_season):
        super().__init__(name, height, age_d)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self):
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def grow(self):
        super().grow()
       # self.nutritional_value += 1

    def age(self):
        super().age()
        self.nutritional_value += 1


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    F1 = Flower("Rose", 15.0, 10, "red")
    F1.show()
    print("[asking the rose to bloom]")
    F1.bloom()
    F1.show()
    
    print()

    print("=== Tree")
    T1 = Tree("Oak", 200.0, 365, 5.0)
    T1.show()
    print("[asking the oak to produce shade]")
    T1.produce_shade()

    print()

    print("=== Vegetable")
    V1 = Vegetable("Tomato", 5.0, 10, "April")
    V1.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        V1.grow()
        V1.age()
    V1.show()
