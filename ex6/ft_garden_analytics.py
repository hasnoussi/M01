#!/usr/bin/env python3
class Plant:
    stats = {"grow": 0, "age": 0, "show": 0}

    @classmethod
    def get_stats(cls):
        return cls.stats
    @staticmethod
    def format_stats(stats):
        texte = ""
        premier = True
        for methode in stats:
            nombre = stats[methode]
            if premier:
                texte += f"{nombre} {methode}"
                premier = False
            else:
                texte += f", {nombre} {methode}"
        return texte
    
    @classmethod
    def display_stats(cls):
        texte = cls.format_stats(cls.get_stats())
        print(f"Stats: {texte}")

        #for enfant in cls.__subclasses__():
         #  enfant.display_stats()

    def __init__(self, name, height, age_d):
        self.name = name 
        self._height = height
        self._age_d = age_d
    
    def grow(self):
        self._height = round(self._height + 0.8, 1)
        type(self).stats["grow"] += 1
    def age(self):
        self._age_d = self._age_d + 1
        type(self).stats["age"] += 1
    def show(self):
        print(f"{self.name}: {self._height}cm, {self._age_d} days old")
        type(self).stats["show"] += 1
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
    
    @staticmethod
    def is_valid_age(_age_d):
        if _age_d > 365:
            print(f"Is {_age_d} days more than a year? -> True")
        else:
            print(f"Is {_age_d} days more than a year? -> False")
    

    @classmethod
    def create_anonym(cls):
        return cls("Unknown plant", 0.0, 0)
    


class Flower(Plant):
    stats = {"grow": 0, "age": 0, "show": 0}

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

class Seed (Flower):
    stats = {"grow": 0, "age": 0 ,"show": 0}

    def __init__(self, name, height, age_d, color, seeds=0):
        super().__init__(name, height, age_d, color)
        self.seeds = seeds

    def bloom(self, seeds):
        super().bloom()
        self.seeds = seeds

    def show(self):
        super().show()
        print(f" Seeds: {self.seeds}")


class Tree (Plant):
    stats = {"grow": 0, "age": 0, "show": 0, "shade": 0}


    def __init__(self, name, height, age_d, trunk_diameter):
        super().__init__(name, height, age_d)
        self.trunk_diameter = trunk_diameter
    
    def show(self):
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self):
        Tree.stats["shade"] += 1
        print(f"Tree {self.name} now produces a shade of {self._height}cm long and {self.trunk_diameter} wide.")

    @classmethod
    def display_stats(cls):
        print(f"Stats: {cls.stats['grow']} grow, "
              f"{cls.stats['age']} age, "
              f"{cls.stats['show']} show")
        print(f"{cls.stats['shade']} shade")
    #def statistic(self):
     #   super().display_stats()
      #  print(f"{Tree.stats['shade']} shade")



class Vegetable (Plant):
    stats = {"grow": 0, "age": 0, "show": 0}

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
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.is_valid_age(30)
    Plant.is_valid_age(400)
    print()
 
    print("=== Flower")
    F1 = Flower("Rose", 15.0, 10, "red")
    F1.show()
    print("[statistics for Rose]")
    F1.display_stats()
    print("[asking the rose to grow and bloom]")
    F1.grow()
    F1.bloom()
    F1.show()
    print("[statistics for Rose]")
    F1.display_stats()

 
    print()
 
    print("=== Tree")
    T1 = Tree("Oak", 200.0, 365, 5.0)
    T1.show()
    print("[statistics for Oak]")
    T1.display_stats()
    print("[asking the oak to produce shade]")
    T1.produce_shade()
    print("[statistics for Oak]")
    T1.display_stats()

 
    print()
    print("=== Seed")
    S1 = Seed("Sunflower", 80.0, 45, "yellow")
    S1.show()
    print("[make sunflower grow, age and bloom]")
    S1.grow()
    S1.age()
    S1.bloom(42)
    S1.show()
    print("[statistics for Sunflower]")
    S1.display_stats()
    print()

    print("=== Anonymous")
    Plant.create_anonym().show()
    print("[statistics for Unknown plant]")
    Plant.display_stats()