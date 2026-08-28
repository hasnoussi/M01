#!/usr/bin/env python3
def ft_garden_intro(name, height, age):
    print("=== Welcome to My Garden ===")
    print("Plant:", name)
    print(f"Height: {height}cm")
    print(f"Age: {age} days")


    print("=== End of Program ===")
if __name__ == "__main__":
    # dans le cas ou on vas pas utiliser une class on devrait faire quelque chose comme ca, ca devient injerable par la suite 
    
    name = "Rose"
    height = 25
    age = 30
    ft_garden_intro(name, height, age)
