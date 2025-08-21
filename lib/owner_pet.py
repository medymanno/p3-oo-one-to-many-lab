# lib/owner_pet.py

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Return a list of this owner's pets"""
        return [pet for pet in Pet.all if pet.owner is self]

    def add_pet(self, pet):
        """Assign this owner to the given pet"""
        if not isinstance(pet, Pet):
            raise Exception("Can only add a Pet instance.")
        pet.owner = self

    def get_sorted_pets(self):
        """Return pets sorted alphabetically by name"""
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    # allowed types
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    # store all pets
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}")

        self.name = name
        self.pet_type = pet_type
        self.owner = None  # default
        if owner:
            if not isinstance(owner, Owner):
                raise Exception("Owner must be an instance of Owner class.")
            self.owner = owner

        Pet.all.append(self)
