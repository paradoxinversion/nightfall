from map_objects.building import Building, building_schematics


def generate_building(schematic):
    """Generates a building with a given schematic"""
    new_building = Building(schematic)
    return new_building
