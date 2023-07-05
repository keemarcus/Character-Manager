# import JSONEncoder to set up our custom encoder
from json import JSONEncoder


class Spell:
    # constructor
    def __init__(self, index, user_id, name, level, classes, subclasses, school, casting_time, range, duration,
                 components, material, concentration, desc, ritual, dc, higher_level, damage, area_of_effect,
                 heal_at_slot_level, attack_type):
        self._index = index
        self._user_id = user_id
        self._name = name
        self._level = level
        self._classes = classes
        self._subclasses = subclasses
        self._school = school
        self._casting_time = casting_time
        self._range = range
        self._duration = duration
        self._components = components
        self._material = material
        self._concentration = concentration
        self._desc = desc
        self._ritual = ritual
        self._dc = dc
        self._higher_level = higher_level
        self._damage = damage
        self._area_of_effect = area_of_effect
        self._heal_at_slot_level = heal_at_slot_level
        self._attack_type = attack_type

    # getters
    def get_index(self):
        return self._index

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_level(self):
        return self._level

    def get_classes(self):
        return self._classes

    def get_subclasses(self):
        return self._subclasses

    def get_school(self):
        return self._school

    def get_casting_time(self):
        return self._casting_time

    def get_range(self):
        return self._range

    def get_duration(self):
        return self._duration

    def get_components(self):
        return self._components

    def get_material(self):
        return self._material

    def get_concentration(self):
        return self._concentration

    def get_desc(self):
        return self._desc

    def get_ritual(self):
        return self._ritual

    def get_dc(self):
        return self._dc

    def get_higher_level(self):
        return self._higher_level

    def get_damage(self):
        return self._damage

    def get_area_of_effect(self):
        return self._area_of_effect

    def get_heal_at_slot_level(self):
        return self._heal_at_slot_level

    def get_attack_type(self):
        return self._attack_type

    # setters
    def set_index(self, index):
        self._index = index

    def set_user_id(self, user_id):
        self._user_id = user_id

    def set_name(self, name):
        self._name = name

    def set_level(self, level):
        self._level = level

    def set_classes(self, classes):
        self._classes = classes

    def set_subclasses(self, subclasses):
        self._subclasses = subclasses

    def set_school(self, school):
        self._school = school

    def set_casting_time(self, casting_time):
        self._casting_time = casting_time

    def set_range(self, range):
        self._range = range

    def set_duration(self, duration):
        self._duration = duration

    def set_components(self, components):
        self._components = components

    def set_material(self, material):
        self._material = material

    def set_concentration(self, concentration):
        self._concentration = concentration

    def set_desc(self, desc):
        self._desc = desc

    def set_ritual(self, ritual):
        self._ritual = ritual

    def set_dc(self, dc):
        self._dc = dc

    def set_higher_level(self, higher_level):
        self._higher_level = higher_level

    def set_damage(self, damage):
        self._damage = damage

    def set_area_of_effect(self, area_of_effect):
        self._area_of_effect = area_of_effect

    def set_heal_at_slot_level(self, heal_at_slot_level):
        self._heal_at_slot_level = heal_at_slot_level

    def set_attack_type(self, attack_type):
        self._attack_type = attack_type


# custom encoder
class SpellEncoder(JSONEncoder):
    # override the default method
    def default(self, spell):
        if isinstance(spell, Spell):
            return spell.__dict__
        else:
            return super.default(self, spell)
