from map_objects.building import Building, building_schematics


def generate_building(schematic, x, y):
    """Generates a building with a given schematic"""
    new_building = Building(schematic, x, y)
    return new_building
