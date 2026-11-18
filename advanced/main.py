
from dataclasses import dataclass

@dataclass
class Creature:
    name: str
    species: str
    level: int
    health: float


while True:
    insert_name = input("Insert creature name: ")
    if insert_name.strip() == "":
        print("Invalid input")
    else:
        break
while True:
    insert_species = input("Insert creature species: ")
    if insert_species.strip() == "":
        print("Invalid input")
    else:
        break
while True:
    try:
        insert_level = int(input("Insert creature level: "))
        break
    except ValueError:
        print("Invalid input")
while True:
    try:
        insert_health = float(input("Insert creature health: "))
        break
    except ValueError:
        print("Invalid input")

creature = Creature(insert_name, insert_species, insert_level, insert_health)

print("Your creature:")
print("Name:", creature.name)
print("Species:", creature.species)
print("Level:", creature.level)
print("Health:", creature.health)
