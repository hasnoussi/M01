#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, age_d: int) -> None:
        self.name = name
        self.height = height
        self.age_d = age_d

    def grow(self) -> None:
        self.height = round(self.height + 0.8, 1)

    def age(self) -> None:
        self.age_d = self.age_d + 1

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_d} days old")

    def track_week(self) -> None:
        self.show()
        height_debut = self.height
        for i in range(7):
            print(f"=== Day {i + 1} ===")
            self.age()
            self.grow()
            self.show()
        croissance = round(self.height - height_debut, 1)
        print(f"Growth this week: {croissance}cm")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    p1 = Plant("Rose", 25.0, 30)
    p2 = Plant("Oak", 200.0, 365)
    p3 = Plant("Cactus", 5.0, 90)
    p4 = Plant("Sunflower", 80.0, 45)
    p5 = Plant("Fern", 15.0, 120)

    garden = [p1, p2, p3, p4, p5]

    for plant in garden:
        print("Created: ", end="")
        plant.show()
