# import our reimbursement dao logic
import pyodbc
import requests

import src.dao.spellbook_dao as dao

# import our reimbursement logic
from src.models.spellbook import SpellBook


# we don't need any business logic for this function, so we simply call our dao function
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
    db_spellbook_spells = dao.get_spellbook_spells(spellbook_id)

    spells = ''
    for row in db_spellbook_spells:
        spells += row[2] + ','

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
    db_spellbook_spells = dao.get_spellbook_spells()

    spells = ''
    for row in db_spellbook_spells:
        spells += row[2] + ','

    # return the result
    return spells


def add_spell(spellbook_id, spell_index):
    # check to see if the spell already exists in the spellbook
    if type(dao.get_spellbook_spell(spellbook_id, spell_index)) == pyodbc.Row:
        return "That spell already exists in that spellbook"
    dao.add_spell(spellbook_id, spell_index)


def delete_spell(spellbook_id, spell_index):
    # check to see if the spell exists in the spellbook
    if type(dao.get_spellbook_spell(spellbook_id, spell_index)) != pyodbc.Row:
        return "That spell doesn't exist in that spellbook"
    dao.delete_spell(spellbook_id, spell_index)


# verify that the selected reimbursement exists then update it using our dao functions
def update_reimbursement(reimbursement_id, amount, reason, date_created):
    # use get reimbursement function to see if the id is associated with an existing reimbursement
    if dao.get_reimbursement(reimbursement_id) is None:
        return "404 Not Found: No such reimbursement exists with that ID", 404
    else:
        # use the update reimbursement function to make the desired changes in the database
        dao.update_reimbursement(reimbursement_id, amount, reason, date_created)

        # return success message
        return "Reimbursement updated successfully.", 201