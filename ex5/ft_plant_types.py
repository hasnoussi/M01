#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, age_d: int) -> None:
        self.name = name
        self._height = height
        self._age_d = age_d

    def grow(self) -> None:
        self._height = round(self._height + 0.8, 1)

    def age(self) -> None:
        self._age_d = self._age_d + 1

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age_d} days old")

    def track_week(self) -> None:
        self.show()
        height_debut = self._height
        for i in range(7):
            print(f"=== Day {i + 1} ===")
            self.age()
            self.grow()
            self.show()
        croissance = round(self._height - height_debut, 1)
        print(f"Growth this week: {croissance}cm")

    def set_height(self, nouvelle_valeur: float) -> None:
        if nouvelle_valeur >= 0:
            self._height = nouvelle_valeur
            print(f"Height updated: {self._height:.0f}cm")
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, nouvelle_valeur: int) -> None:
        if nouvelle_valeur >= 0:
            self._age_d = nouvelle_valeur
            print(f"Age updated: {nouvelle_valeur} days")
            print()
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            print()

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_d


class Flower(Plant):
    def __init__(
        self, name: str, height: float, age_d: int, color: str
    ) -> None:
        super().__init__(name, height, age_d)
        self.color = color
        self.bloomed = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")

    def bloom(self) -> None:
        self.bloomed = True


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age_d: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age_d)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self._height}cm long and {self.trunk_diameter}cm wide."
        )


class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, age_d: int, harvest_season: str
    ) -> None:
        super().__init__(name, height, age_d)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def grow(self) -> None:
        super().grow()

    def age(self) -> None:
        super().age()
        self.nutritional_value += 1


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    f1 = Flower("Rose", 15.0, 10, "red")
    f1.show()
    print("[asking the rose to bloom]")
    f1.bloom()
    f1.show()

    print()

    print("=== Tree")
    t1 = Tree("Oak", 200.0, 365, 5.0)
    t1.show()
    print("[asking the oak to produce shade]")
    t1.produce_shade()

    print()

    print("=== Vegetable")
    v1 = Vegetable("Tomato", 5.0, 10, "April")
    v1.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        v1.grow()
        v1.age()
    v1.show()
