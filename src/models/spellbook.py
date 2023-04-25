# import JSONEncoder to set up our custom encoder
from json import JSONEncoder


class SpellBook:
    # constructor
    def __init__(self, spellbook_id, user_id, character_id, spell_casting_class, spell_casting_level, spells=[None]):
        self._spellbook_id = spellbook_id
        self._user_id = user_id
        self._character_id = character_id
        self._spell_casting_class = spell_casting_class
        self._spell_casting_level = spell_casting_level
        self._spells = spells

    # getters
    def get_spellbook_id(self):
        return self._spellbook_id

    def get_user_id(self):
        return self._user_id

    def get_character_id(self):
        return self._character_id

    def get_spell_casting_class(self):
        return self._spell_casting_class

    def get_spell_casting_level(self):
        return self._spell_casting_level

    def get_spells(self):
        return self.spells

    # setters
    def set_spellbook_id(self, spellbook_id):
        self._spellbook_id = spellbook_id

    def set_user_id(self, user_id):
        self._user_id = user_id

    def set_character_id(self, character_id):
        self._character_id = character_id

    def set_spell_casting_class(self, spell_casting_class):
        self._spell_casting_class = spell_casting_class

    def set_spell_casting_level(self, spell_casting_level):
        self._spell_casting_level = spell_casting_level

    def set_spells(self, spells):
        self._spells = spells


# custom encoder
class SpellbookEncoder(JSONEncoder):
    # override the default method
    def default(self, spellbook):
        if isinstance(spellbook, SpellBook):
            return spellbook.__dict__
        else:
            return JSONEncoder.default(self, spellbook)
