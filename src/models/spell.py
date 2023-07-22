# import JSONEncoder to set up our custom encoder
from json import JSONEncoder


class Spell:
    # constructor
    def __init__(self, _index, _user_id, _name, _level, _classes, _subclasses, _school, _casting_time, _range,
                 _duration, _components, _material, _concentration, _desc, _ritual, _dc, _higher_level, _damage,
                 _area_of_effect, _heal_at_slot_level, _attack_type):
        self.index = _index
        self.user_id = _user_id
        self.name = _name
        self.level = _level
        self.classes = _classes
        self.subclasses = _subclasses
        self.school = _school
        self.casting_time = _casting_time
        self.range = _range
        self.duration = _duration
        self.components = _components
        self.material = _material
        self.concentration = _concentration
        self.desc = _desc
        self.ritual = _ritual
        self.dc = _dc
        self.higher_level = _higher_level
        self.damage = _damage
        self.area_of_effect = _area_of_effect
        self.heal_at_slot_level = _heal_at_slot_level
        self.attack_type = _attack_type

    # getters
    def get_index(self):
        return self.index

    def get_user_id(self):
        return self.user_id

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_classes(self):
        return self.classes

    def get_subclasses(self):
        return self.subclasses

    def get_school(self):
        return self.school

    def get_casting_time(self):
        return self.casting_time

    def get_range(self):
        return self.range

    def get_duration(self):
        return self.duration

    def get_components(self):
        return self.components

    def get_material(self):
        return self.material

    def get_concentration(self):
        return self.concentration

    def get_desc(self):
        return self.desc

    def get_ritual(self):
        return self.ritual

    def get_dc(self):
        return self.dc

    def get_higher_level(self):
        return self.higher_level

    def get_damage(self):
        return self.damage

    def get_area_of_effect(self):
        return self.area_of_effect

    def get_heal_at_slot_level(self):
        return self.heal_at_slot_level

    def get_attack_type(self):
        return self.attack_type

    # setters
    def set_index(self, index):
        self.index = index

    def set_user_id(self, user_id):
        self.user_id = user_id

    def set_name(self, name):
        self.name = name

    def set_level(self, level):
        self.level = level

    def set_classes(self, classes):
        self.classes = classes

    def set_subclasses(self, subclasses):
        self.subclasses = subclasses

    def set_school(self, school):
        self.school = school

    def set_casting_time(self, casting_time):
        self.casting_time = casting_time

    def set_range(self, range):
        self.range = range

    def set_duration(self, duration):
        self.duration = duration

    def set_components(self, components):
        self.components = components

    def set_material(self, material):
        self.material = material

    def set_concentration(self, concentration):
        self.concentration = concentration

    def set_desc(self, desc):
        self.desc = desc

    def set_ritual(self, ritual):
        self.ritual = ritual

    def set_dc(self, dc):
        self.dc = dc

    def set_higher_level(self, higher_level):
        self.higher_level = higher_level

    def set_damage(self, damage):
        self.damage = damage

    def set_area_of_effect(self, area_of_effect):
        self.area_of_effect = area_of_effect

    def set_heal_at_slot_level(self, heal_at_slot_level):
        self.heal_at_slot_level = heal_at_slot_level

    def set_attack_type(self, attack_type):
        self.attack_type = attack_type


# custom encoder
class SpellEncoder(JSONEncoder):
    # override the default method
    def default(self, spell):
        if isinstance(spell, Spell):
            return spell.__dict__
        else:
            return super.default(self, spell)
