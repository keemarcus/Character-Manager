# import JSONEncoder to set up our custom encoder
from json import JSONEncoder


class Character:
    # constructor
    def __init__(self, _name, _str_score, _dex_score, _con_score, _int_score, _wis_score, _cha_score, _user_id):
        self.name = _name
        self.str_score = _str_score
        self.dex_score = _dex_score
        self.con_score = _con_score
        self.int_score = _int_score
        self.wis_score = _wis_score
        self.cha_score = _cha_score
        self.user_id = _user_id

    # getters
    def get_name(self):
        return self.name

    def get_str(self):
        return self.str_score

    def get_dex(self):
        return self.dex_score

    def get_con(self):
        return self.con_score

    def get_int(self):
        return self.int_score

    def get_wis(self):
        return self.wis_score

    def get_cha(self):
        return self.cha_score

    def get_user_id(self):
        return self.user_id

    # setters
    def set_name(self, name):
        self.name = name

    def set_str(self, str_score):
        self.str_score = str_score

    def set_dex(self, dex_score):
        self.dex_score = dex_score

    def set_con(self, con_score):
        self.con_score = con_score

    def set_int(self, int_score):
        self.int_score = int_score

    def set_wis(self, wis_score):
        self.wis_score = wis_score

    def set_cha(self, cha_score):
        self.cha_score = cha_score

    def set_user_id(self, user_id):
        self.user_id = user_id


# custom encoder
class CharacterEncoder(JSONEncoder):
    # override the default method
    def default(self, character):
        if isinstance(character, Character):
            return character.__dict__
        else:
            return JSONEncoder.default(self, character)
