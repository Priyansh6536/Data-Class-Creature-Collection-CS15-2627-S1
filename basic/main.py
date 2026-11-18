
from dataclasses import dataclass

@dataclass
class Creature:
    name: str
    species: str
    level: int
    health: float


creature1 = Creature("Drake", "Dragon", 15, 100.0)
creature2 = Creature("Shadow", "Wolf", 12, 85.5)
creature3 = Creature("Aqua", "Mermaid", 20, 120.0)


print("Creature 1:")

print("Name:", creature1.name)
print("Species:", creature1.species)
print("Level:", creature1.level)
print("Health:", creature1.health)

print("\nCreature 2:")

print("Name:", creature2.name)
print("Species:", creature2.species)
print("Level:", creature2.level)
print("Health:", creature2.health)


print("\nCreature 3:")

print("Name:", creature3.name)
print("Species:", creature3.species)
print("Level:", creature3.level)
print("Health:", creature3.health)



creature1.level = 18
creature1.health = 150.0


print("\nUpdated Creature 1:")


print("Name:", creature1.name)
print("Species:", creature1.species)
print("Level:", creature1.level)
print("Health:", creature1.health)



print("\nOther Creatures:")

print("Creature 2 Level:", creature2.level)
print("Creature 2 Health:", creature2.health)
print("Creature 3 Level:", creature3.level)
print("Creature 3 Health:", creature3.health)
