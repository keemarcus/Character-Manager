# import our get connection function
from utils import dbconfig


# add a new spell to the database
def create_spell(spell):
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string using parameterization to protect against SQL injection
        query = "INSERT INTO spells VALUES (?, 0, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        # execute our query and commit the changes to the database
        cursor.execute(query, spell.get_index(), spell.get_name(), spell.get_level(), spell.get_classes(),
                       spell.get_subclasses(), spell.get_school(), spell.get_casting_time(), spell.get_range(),
                       spell.get_duration(), spell.get_components(), spell.get_material(), spell.get_concentration(),
                       spell.get_desc(), spell.get_ritual(), spell.get_dc(), spell.get_higher_level(),
                       spell.get_damage(), spell.get_area_of_effect(), spell.get_heal_at_slot_level(),
                       spell.get_attack_type())
        cursor.commit()
    finally:
        # close our database connection
        connection.close()
    return "Adding Spell: " + spell.get_name()


# pull a specific spell from the database
def get_spell(spell_index):
    # create result variable
    result = None
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string using parameterization to protect against SQL injection
        query = "SELECT * FROM spells WHERE spell_index = ?"
        # execute our query
        cursor.execute(query, spell_index)
        # fetch the results of the query
        result = cursor.fetchone()
    finally:
        # close our database connection
        connection.close()
        # return the result
        return result


# pull all the available spells for a given class
def get_spells(class_name, user_id=None, level=None):
    # create result variable
    result = None
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        if level:
            # create query string using parameterization to protect against SQL injection
            query = "SELECT * FROM spells WHERE spell_classes like ? and user_id = 0  and spell_level <= ? " \
                    "ORDER BY spell_level ASC"
            # execute our query
            cursor.execute(query, '%' + class_name + '%', level)
        else:
            # create query string using parameterization to protect against SQL injection
            query = "SELECT * FROM spells WHERE spell_classes like ? and user_id = 0 ORDER BY spell_level ASC"
            # execute our query
            cursor.execute(query, '%' + class_name + '%')
        # fetch the results of the query
        result = cursor.fetchall()
    finally:
        # close our database connection
        connection.close()
        # return the result
        return result
