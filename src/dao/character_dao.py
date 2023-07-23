# import our get connection function
from utils import dbconfig


# add a new character to the database
def create_character(character):
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string using parameterization to protect against SQL injection
        query = "INSERT INTO chars VALUES (default, ?, ?, ?, ?, ?, ?, ?, ?)"
        # execute our query and commit the changes to the database
        cursor.execute(query, character.get_name(), character.get_user_id(), character.get_str(), character.get_dex(),
                       character.get_con(), character.get_int(), character.get_wis(), character.get_cha())
        cursor.commit()
    finally:
        # close our database connection
        connection.close()
    return "Adding Character: " + character.get_name()


# pull a specific character from the database
def get_character(spell_index):
    # create result variable
    result = None
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string using parameterization to protect against SQL injection
        query = "SELECT * FROM chars WHERE character_id = ?"
        # execute our query
        cursor.execute(query, spell_index)
        # fetch the results of the query
        result = cursor.fetchone()
    finally:
        # close our database connection
        connection.close()
        # return the result
        return result
