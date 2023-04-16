# import JSONEncoder to set up our custom encoder
from json import JSONEncoder


class Spell:
    # constructor
    def __init__(self, index, name, desc, spell_range, components, duration, concentration, casting_time, level, school,
                 classes, subclasses, dc, higher_level, ritual, damage, attack_type):
        self._index = index
        self._name = name
        self._desc = desc
        self._spell_range = spell_range
        self._components = components
        self._duration = duration
        self._concentration = concentration
        self._casting_time = casting_time
        self._level = level
        self._school = school
        self._classes = classes
        self._subclasses = subclasses
        self._dc = dc
        self._higher_level = higher_level
        self._ritual = ritual
        self._damage = damage
        self._attack_type = attack_type

    # getters
    def get_index(self):
        return self._index

    def get_name(self):
        return self._name

    def get_desc(self):
        return self._desc

    def get_range(self):
        return self._spell_range

    def get_components(self):
        return self._components

    def get_duration(self):
        return self._duration

    def get_concentration(self):
        return self._concentration

    def get_casting_time(self):
        return self._casting_time

    def get_level(self):
        return self._level

    def get_school(self):
        return self._school

    def get_classes(self):
        return self._classes

    def get_subclasses(self):
        return self._subclasses

    def get_dc(self):
        return self._dc

    def get_higher_level(self):
        return self._higher_level

    def get_ritual(self):
        return self._ritual

    def get_damage(self):
        return self._damage

    def get_attack_type(self):
        return self._attack_type

    # setters
    def set_index(self, index):
        self._index = index

    def set_name(self, name):
        self._name = name

    def set_desc(self, desc):
        self._desc = desc

    def set_range(self):
        self._spell_range = range

    def set_components(self, components):
        self._components = components

    def set_duration(self, duration):
        self._duration = duration

    def set_concentration(self, concentration):
        self._concentration = concentration

    def set_casting_time(self,casting_time):
        self._casting_time = casting_time

    def set_level(self, level):
        self._level = level

    def set_school(self, school):
        self._school = school

    def set_classes(self, classes):
        self._classes = classes

    def set_subclasses(self, subclasses):
        self._subclasses = subclasses

    def set_dc(self, dc):
        self._dc = dc

    def set_higher_level(self, higher_level):
        self._higher_level = higher_level

    def set_ritual(self, ritual):
        self._ritual = ritual

    def set_damage(self, damage):
        self._damage = damage

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
