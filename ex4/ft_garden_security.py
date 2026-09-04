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


if __name__ == "__main__":
    print("=== Garden Security System ===")
    p1 = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    p1.show()
    print()

    p1.set_height(25.0)
    p1.set_age(30)
    p1.get_height()
    p1.get_age()
    p1.set_height(-5)
    p1.set_age(-45)

    print("Current state: ", end="")
    p1.show()
