# import JSONEncoder to set up our custom encoder
from json import JSONEncoder


class Character:
    # constructor
    def __init__(self, name, str_score, dex_score, con_score, int_score, wis_score, cha_score):
        self._name = name
        self._str_score = str_score
        self._dex_score = dex_score
        self._con_score = con_score
        self._int_score = int_score
        self._wis_score = wis_score
        self._cha_score = cha_score

    # getters
    def get_name(self):
        return self._name

    def get_str(self):
        return self._str_score

    def get_dex(self):
        return self._dex_score

    def get_con(self):
        return self._con_score

    def get_int(self):
        return self._int_score

    def get_wis(self):
        return self._wis_score

    def get_cha(self):
        return self._cha_score

    # setters
    def set_name(self, name):
        self._name = name

    def set_str(self, str_score):
        self._str_score = str_score

    def set_dex(self, dex_score):
        self._dex_score = dex_score

    def set_con(self, con_score):
        self._con_score = con_score

    def set_int(self, int_score):
        self._int_score = int_score

    def set_wis(self, wis_score):
        self._wis_score = wis_score

    def set_cha(self, cha_score):
        self._cha_score = cha_score


# custom encoder
class CharacterEncoder(JSONEncoder):
    # override the default method
    def default(self, character):
        if isinstance(character, Character):
            return character.__dict__
        else:
            return JSONEncoder.default(self, character)
