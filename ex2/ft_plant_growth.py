#!/usr/bin/env python3
class Plant:
    def __init__(self, name, height, age_d):
        self.name = name 
        self.height = height
        self.age_d = age_d
    
    def grow(self):
        self.height = round(self.height + 0.8, 1)
    def age(self):
        self.age_d = self.age_d + 1
    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age_d} days old")
    def  track_week(self):
        self.show()
        height_debut = self.height
        for i in range(7):
            print(f"=== Day {i + 1} ===")
            self.age()
            self.grow()
            self.show()
        croissance = round(self.height - height_debut, 1)
        print(f"Growth this week: {croissance}cm")
       
print("=== Garden Plant Registry ===") 
if __name__ == "__main__":
   
    p1 = Plant("Rose", 15.0, 10) 

    p1.track_week() 