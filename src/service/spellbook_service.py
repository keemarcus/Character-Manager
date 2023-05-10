# import our reimbursement dao logic
import pyodbc
import requests

import src.dao.spellbook_dao as dao

# import our reimbursement logic
from src.models.spellbook import SpellBook


# call get reimbursement function from dao layer and convert it to usable data
def get_spellbook_slots(spellbook_id):
    # get result from dao
    db_spell_slots = dao.get_spell_slots(spellbook_id)
    if db_spell_slots is None:
        return None

    spell_slots = {}
    for row in db_spell_slots:
        spell_slots[str(row[2]) + "_available"] = row[4]
        spell_slots[str(row[2]) + "_total"] = row[3]
    return spell_slots


def restore_spell_slots(spellbook_id):
    # validate spellbook id
    if dao.get_spellbook(spellbook_id) is None:
        return "That spellbook does not exist", 400
    dao.restore_all_spell_slots(spellbook_id)


def cast_spell(character_id, spellbook_id, spell_index, spell_level):
    # validate character id
    if dao.get_character(character_id) is None:
        return "That spellbook does not exists", 400
    # validate spellbook id
    if dao.get_spellbook(spellbook_id) is None:
        return "That spellbook does not exist", 400
    # validate spell
    if (requests.get("https://www.dnd5eapi.co/api/spells/" + spell_index).status_code // 100) != 2:
        return "That spell does not exist", 400
    # check to see if the spell exists in the spellbook
    if type(dao.get_spellbook_spell(spellbook_id, spell_index)) != pyodbc.Row:
        return "That spell does not exists in that spellbook", 400
    # check to make sure the spell can be cast at the given level
    if requests.get("https://www.dnd5eapi.co/api/spells/" + spell_index).json()["level"] > spell_level:
        return "That spell cannot be cast at that level", 400
    # check to make sure the character has a spell slot available at the given level
    if not dao.check_for_spell_slot(spellbook_id, spell_level):
        return "No spell slots available at that level", 400
    # remove one available spell slot at the given level
    dao.expend_spell_slot(spellbook_id, spell_level)
    return "Spell cast successfully", 200


def create_spellbook(user_id, character_id, spell_casting_class, spell_casting_level, spellbook_id="default"):
    # validate user id
    if dao.get_user(user_id) is None:
        return "That user does not exist"
    # validate character id
    if dao.get_character(character_id) is not None:
        return "That spellbook already exists"
    # validate class
    if (requests.get("https://www.dnd5eapi.co/api/classes/" + spell_casting_class).status_code // 100) != 2:
        return "That class does not exist"
    # validate level
    if spell_casting_level < 1 or spell_casting_level > 20:
        return "That spellcasting level is invalid"
    dao.create_spellbook(user_id, character_id, spell_casting_class, spell_casting_level, spellbook_id)


def delete_spellbook(spellbook_id):
    # validate spellbook id
    if dao.get_spellbook(spellbook_id) is None:
        return "That spellbook does not exist"
    dao.delete_spellbook(spellbook_id)


def update_spellbook(spellbook_id, user_id, character_id, spell_casting_class, spell_casting_level):
    # validate spellbook id
    if dao.get_spellbook(spellbook_id) is None:
        return "That spellbook does not exist"
    # validate user id
    if dao.get_user(user_id) is None:
        return "That user does not exist"
    # validate character id
    if dao.get_character(character_id) is None:
        return "That spellbook does not exist"
    # validate class
    if (requests.get("https://www.dnd5eapi.co/api/classes/" + spell_casting_class).status_code // 100) != 2:
        return "That class does not exist"
    # validate level
    if spell_casting_level < 1 or spell_casting_level > 20:
        return "That spellcasting level is invalid"
    dao.update_spellbook(spellbook_id, user_id, character_id, spell_casting_class, spell_casting_level)


# call get reimbursement function from dao layer and convert it to usable data
def get_spellbook(spellbook_id):
    # get result from dao
    db_spellbook = dao.get_spellbook(spellbook_id)
    if db_spellbook is None:
        return None
    db_spellbook_spells = dao.get_spellbook_spells(spellbook_id)

    spells = ''
    for row in db_spellbook_spells:
        spells += row[2] + ','
    if len(spells) > 0:
        spells = spells[:-1]

    # create a Spellbook object for the result
    spellbook = SpellBook(
        db_spellbook[0],
        db_spellbook[1],
        db_spellbook[2],
        db_spellbook[3],
        db_spellbook[4],
        spells
    )

    # return the result
    return spellbook


def get_spellbook_spells(spellbook_id=None):
    # dao.get_spellbook_spells()
    # get results from dao
    db_spellbook_spells = dao.get_spellbook_spells(spellbook_id)
    spells = ''
    for row in db_spellbook_spells:
        spells += row[2] + ','
    spells = spells[:-1]

    # return the result
    return spells


def add_spell(spellbook_id, spell_index, spell_level):
    # validate spell
    if (requests.get("https://www.dnd5eapi.co/api/spells/" + spell_index).status_code // 100) != 2:
        return "That spell does not exist"
    # check to see if the spell already exists in the spellbook
    if type(dao.get_spellbook_spell(spellbook_id, spell_index)) == pyodbc.Row:
        return "That spell already exists in that spellbook"
    dao.add_spell(spellbook_id, spell_index, spell_level)


def delete_spell(spellbook_id, spell_index):
    # check to see if the spell exists in the spellbook
    if type(dao.get_spellbook_spell(spellbook_id, spell_index)) != pyodbc.Row:
        return "That spell doesn't exist in that spellbook"
    dao.delete_spell(spellbook_id, spell_index)
