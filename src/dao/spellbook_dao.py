# import our get connection function
from utils import dbconfig


# expend spell slot
def expend_spell_slot(spellbook_id, spell_level):
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string using parameterization to protect against SQL injection
        query = "UPDATE spellSlots SET slots_available = slots_available - 1 WHERE spellbook_id = ? AND spell_level = ?"
        # execute our query
        cursor.execute(query, spellbook_id, spell_level)
        cursor.commit()
    finally:
        # close our database connection
        connection.close()
        # return the result


# restore spell slot
def restore_spell_slot(spellbook_id, spell_level):
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string using parameterization to protect against SQL injection
        query = "UPDATE spellSlots SET slots_available = slots_available + 1 WHERE spellbook_id = ? AND spell_level = ?"
        # execute our query
        cursor.execute(query, spellbook_id, spell_level)
        cursor.commit()
    finally:
        # close our database connection
        connection.close()
        # return the result


# restore all spell slots
def restore_all_spell_slots(spellbook_id):
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string using parameterization to protect against SQL injection
        query = "UPDATE spellSlots SET slots_available = slots_total WHERE spellbook_id = ?"
        # execute our query
        cursor.execute(query, spellbook_id)
        cursor.commit()
    finally:
        # close our database connection
        connection.close()
        # return the result


# check spell slot
def check_for_spell_slot(spellbook_id, spell_level):
    # create result variable
    result = None
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string using parameterization to protect against SQL injection
        query = "SELECT slots_available FROM spellSlots WHERE spellbook_id = ? AND spell_level = ?"
        # execute our query
        cursor.execute(query, spellbook_id, spell_level)
        # fetch the results of the query
        result = cursor.fetchone()
    finally:
        # close our database connection
        connection.close()
        # return the result
        return result[0] > 0


# add a new spellbook to the database
def create_spellbook(user_id, character_id, spell_casting_class, spell_casting_level, spellbook_id="default"):
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string using parameterization to protect against SQL injection
        if spellbook_id == "default":
            query = "INSERT INTO spellbooks VALUES (default, ?, ?, ?, ?)"
            # execute our query and commit the changes to the database
            cursor.execute(query, user_id, character_id, spell_casting_class, spell_casting_level)
        else:
            query = "INSERT INTO spellbooks VALUES (?, ?, ?, ?, ?)"
            # execute our query and commit the changes to the database
            cursor.execute(query, spellbook_id, user_id, character_id, spell_casting_class, spell_casting_level)
        cursor.commit()
    finally:
        # close our database connection
        connection.close()


# update an existing spellbook
def update_spellbook(spellbook_id, user_id, character_id, spell_casting_class, spell_casting_level):
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string using parameterization to protect against SQL injection
        query = """UPDATE spellbooks SET user_id = ?, character_id = ?, spell_casting_class = ?, class_level = ? 
                    WHERE spellbook_id = ?"""
        # execute our query and commit the changes to the database
        cursor.execute(query, user_id, character_id, spell_casting_class, spell_casting_level, spellbook_id)
        cursor.commit()
    finally:
        # close our database connection
        connection.close()


# delete an existing spell from a spellbook
def delete_spellbook(spellbook_id):
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string using parameterization to protect against SQL injection
        query = "DELETE FROM spellbooks WHERE spellbook_id = ?"
        # execute our query and commit the changes to the database
        cursor.execute(query, spellbook_id)
        cursor.commit()
    finally:
        # close our database connection
        connection.close()


# pull a specific spellbook from the database
def get_spellbook(spellbook_id):
    # create result variable
    result = None
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string using parameterization to protect against SQL injection
        query = "SELECT * FROM spellbooks WHERE spellbook_id = ?"
        # execute our query
        cursor.execute(query, spellbook_id)
        # fetch the results of the query
        result = cursor.fetchone()
    finally:
        # close our database connection
        connection.close()
        # return the result
        return result


# pull all the spells in a given spellbook
def get_spellbook_spells(spellbook_id=None):
    # create result variable
    result = None
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string
        if spellbook_id is not None:
            query = "SELECT * FROM preparedSpells WHERE spellbook_id = ? ORDER BY prepared_spell_id"
            # execute our query
            cursor.execute(query, spellbook_id)
        else:
            query = "SELECT * FROM preparedSpells ORDER BY prepared_spell_id"
            # execute our query
            cursor.execute(query)

        # use cursor to fetch the results of the query
        result = cursor.fetchall()
    finally:
        # close our database connection
        connection.close()
        # return the result
        return result


# pull a specific spell from a given spellbook
def get_spellbook_spell(spellbook_id, spell_index):
    # create result variable
    result = None
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string
        query = "SELECT * FROM preparedSpells WHERE spellbook_id = ? AND spell_index = ?"
        # execute our query
        cursor.execute(query, spellbook_id, spell_index)
        # use cursor to fetch the results of the query
        result = cursor.fetchone()
    finally:
        # close our database connection
        connection.close()
        # return the result
        return result


# add a new spell to an existing spellbook
def add_spell(spellbook_id, spell_index):
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string using parameterization to protect against SQL injection
        query = "INSERT INTO preparedSpells VALUES (default, ?, ?)"
        # execute our query and commit the changes to the database
        cursor.execute(query, spellbook_id, spell_index)
        cursor.commit()
    finally:
        # close our database connection
        connection.close()


# delete an existing spell from a spellbook
def delete_spell(spellbook_id, spell_index):
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string using parameterization to protect against SQL injection
        query = "DELETE FROM preparedSpells WHERE spellbook_id = ? AND spell_index = ?"
        # execute our query and commit the changes to the database
        cursor.execute(query, spellbook_id, spell_index)
        cursor.commit()
    finally:
        # close our database connection
        connection.close()


def get_user(user_id):
    # create result variable
    result = None
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string
        query = "SELECT * FROM users WHERE user_id = ?"
        # execute our query
        cursor.execute(query, user_id)
        # use cursor to fetch the results of the query
        result = cursor.fetchone()
    finally:
        # close our database connection
        connection.close()
        # return the result
        return result


def get_character(character_id):
    # create result variable
    result = None
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string
        query = "SELECT * FROM spellbooks WHERE character_id = ?"
        # execute our query
        cursor.execute(query, character_id)
        # use cursor to fetch the results of the query
        result = cursor.fetchone()
    finally:
        # close our database connection
        connection.close()
        # return the result
        return result
