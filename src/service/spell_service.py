import src.dao.spell_dao as dao
from src.models.spell import Spell
from utils import dbconfig


def create_spell(index, user_id, name, level, classes, subclasses, school, casting_time, range, duration, components,
                 material, concentration, desc, ritual, dc, higher_level, damage, area_of_effect, heal_at_slot_level,
                 attack_type):
    # check to see if the spell already exists in the database
    result = None
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string
        query = "SELECT * FROM spells WHERE spell_index = ?"
        # execute our query
        cursor.execute(query, index)
        # use cursor to fetch the results of the query
        result = cursor.fetchone()
    finally:
        # close our database connection
        connection.close()

    if result is not None:
        print("Spell: " + name + " - Is Already In Database")
        return str("Spell: " + name + " - Is Already In Database")

    print("Adding Spell: " + name)
    # create a spell object
    new_spell = Spell(index, user_id, name, level, classes, subclasses, school, casting_time, range, duration,
                      components, material, concentration, desc, ritual, dc, higher_level, damage, area_of_effect,
                      heal_at_slot_level, attack_type)
    # call the dao method
    return dao.create_spell(new_spell)


def get_spell(index):
    db_spell = dao.get_spell(index)
    return Spell(db_spell[0], db_spell[1], db_spell[2], db_spell[3], db_spell[4], db_spell[5], db_spell[6], db_spell[7],
                 db_spell[8], db_spell[9], db_spell[10], db_spell[11], db_spell[12], db_spell[13], db_spell[14],
                 db_spell[15], db_spell[16], db_spell[17], db_spell[18], db_spell[19], db_spell[20])


def get_spells(class_name, user_id=None, level=None):
    db_spells = dao.get_spells(class_name, user_id, level)
    spells = list()
    for db_spell in db_spells:
        spells.append(Spell(db_spell[0], db_spell[1], db_spell[2], db_spell[3], db_spell[4], db_spell[5], db_spell[6],
                            db_spell[7], db_spell[8], db_spell[9], db_spell[10], db_spell[11], db_spell[12],
                            db_spell[13], db_spell[14], db_spell[15], db_spell[16], db_spell[17], db_spell[18],
                            db_spell[19], db_spell[20]))
    return spells

