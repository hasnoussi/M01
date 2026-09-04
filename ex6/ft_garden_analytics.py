#!/usr/bin/env python3


class Plant:
    class _Stats:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def record_grow(self) -> None:
            self._grow_count += 1

        def record_age(self) -> None:
            self._age_count += 1

        def record_show(self) -> None:
            self._show_count += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_count} grow, "
                f"{self._age_count} age, {self._show_count} show"
            )

    def __init__(self, name: str, height: float, age_d: int) -> None:
        self.name = name
        self._height = height
        self._age_d = age_d
        self._stats = Plant._Stats()

    def grow(self) -> None:
        self._height = round(self._height + 0.8, 1)
        self._stats.record_grow()

    def age(self) -> None:
        self._age_d += 1
        self._stats.record_age()

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age_d} days old")
        self._stats.record_show()

    def display_stats(self) -> None:
        self._stats.display()

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

    @staticmethod
    def is_valid_age(age_d: int) -> None:
        is_old = age_d > 365
        print(f"Is {age_d} days more than a year? -> {is_old}")

    @classmethod
    def create_anonym(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


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


class Seed(Flower):
    def __init__(
        self, name: str, height: float, age_d: int,
        color: str, seeds: int = 0
    ) -> None:
        super().__init__(name, height, age_d, color)
        self.seeds = seeds

    def bloom(self, seeds: int = 0) -> None:
        super().bloom()
        self.seeds = seeds

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")


class Tree(Plant):
    class _TreeStats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count = 0

        def record_shade(self) -> None:
            self._shade_count += 1

        def display(self) -> None:
            super().display()
            print(f" {self._shade_count} shade")

    def __init__(
        self, name: str, height: float, age_d: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age_d)
        self.trunk_diameter = trunk_diameter
        self._stats: Tree._TreeStats = Tree._TreeStats()

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        self._stats.record_shade()
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

    def age(self) -> None:
        super().age()
        self.nutritional_value += 1


def show_plant_stats(plant: Plant) -> None:
    plant.display_stats()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.is_valid_age(30)
    Plant.is_valid_age(400)
    print()

    print("=== Flower")
    f1 = Flower("Rose", 15.0, 10, "red")
    f1.show()
    print("[statistics for Rose]")
    show_plant_stats(f1)
    print("[asking the rose to grow and bloom]")
    f1.grow()
    f1.bloom()
    f1.show()
    print("[statistics for Rose]")
    show_plant_stats(f1)

    print()

    print("=== Tree")
    t1 = Tree("Oak", 200.0, 365, 5.0)
    t1.show()
    print("[statistics for Oak]")
    show_plant_stats(t1)
    print("[asking the oak to produce shade]")
    t1.produce_shade()
    print("[statistics for Oak]")
    show_plant_stats(t1)

    print()
    print("=== Seed")
    s1 = Seed("Sunflower", 80.0, 45, "yellow")
    s1.show()
    print("[make sunflower grow, age and bloom]")
    s1.grow()
    s1.age()
    s1.bloom(42)
    s1.show()
    print("[statistics for Sunflower]")
    show_plant_stats(s1)
    print()

    print("=== Anonymous")
    anon = Plant.create_anonym()
    anon.show()
    print("[statistics for Unknown plant]")
    show_plant_stats(anon)
