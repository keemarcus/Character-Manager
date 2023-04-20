# import our reimbursement dao logic
import pyodbc

import src.dao.spellbook_dao as dao

# import our reimbursement logic
from src.models.spellbook import SpellBook


# we don't need any business logic for this function, so we simply call our dao function
def create_spellbook(spellbook_id, spell_casting_class, spell_casting_level, spells=[None]):
    dao.create_spellbook(spellbook_id, spell_casting_class, spell_casting_level, spells)


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