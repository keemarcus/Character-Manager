# import JSONEncoder to set up our custom encoder
from json import JSONEncoder


class SpellBook:
    # constructor
    def __init__(self, _spellbook_id, _user_id, _character_id, _spell_casting_class, _spell_casting_level, _spells=None):
        self.spellbook_id = _spellbook_id
        self.user_id = _user_id
        self.character_id = _character_id
        self.spell_casting_class = _spell_casting_class
        self.spell_casting_level = _spell_casting_level
        self.spells = _spells

    # getters
    def get_spellbook_id(self):
        return self.spellbook_id

    def get_user_id(self):
        return self.user_id

    def get_character_id(self):
        return self.character_id

    def get_spell_casting_class(self):
        return self.spell_casting_class

    def get_spell_casting_level(self):
        return self.spell_casting_level

    def get_spells(self):
        return self.spells

    # setters
    def set_spellbook_id(self, spellbook_id):
        self.spellbook_id = spellbook_id

    def set_user_id(self, user_id):
        self.user_id = user_id

    def set_character_id(self, character_id):
        self.character_id = character_id

    def set_spell_casting_class(self, spell_casting_class):
        self.spell_casting_class = spell_casting_class

    def set_spell_casting_level(self, spell_casting_level):
        self.spell_casting_level = spell_casting_level

    def set_spells(self, spells):
        self.spells = spells


# custom encoder
class SpellbookEncoder(JSONEncoder):
    # override the default method
    def default(self, spellbook):
        if isinstance(spellbook, SpellBook):
            return spellbook.__dict__
        else:
            return JSONEncoder.default(self, spellbook)
