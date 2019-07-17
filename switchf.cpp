// Example program
#include <iostream>
#include <string>

enum Animal
{
    Animal_pig,
    Animal_chicken,
    Animal_goat,
    Animal_cat,
    Animal_dog,
    Animal_ostrich
};

std::string getAnimalName(Animal animal)
{
    switch(animal)
    {
        case Animal_pig:
            return "Pig";
        case Animal_chicken:
            return "Chicken";
        case Animal_goat:
            return "Goat";
        case Animal_cat:
            return "Cat";
        case Animal_dog:
            return "Dog";
        case Animal_ostrich:
            return "Ostrich";
        default:
            return "???";
    }
}

int getAnimalLegs(Animal animal)
{
    switch(animal)
    {
        case Animal_chicken:
        case Animal_ostrich:
            return 2;
        case Animal_pig:
        case Animal_goat:
        case Animal_cat:
        case Animal_dog:
            return 4;
    }
}

int main()
{
    std::cout << "A " << getAnimalName(Animal_chicken) << " has " << getAnimalLegs(Animal_chicken) << " legs." << "\n";
    std::cout << "A " << getAnimalName(Animal_pig) << " has " << getAnimalLegs(Animal_pig) << " legs.";
    return 0;
}
