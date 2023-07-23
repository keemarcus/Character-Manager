import src.dao.character_dao as dao
from src.models.character import Character
from utils import dbconfig


def create_character(name, user_id, str_score, dex_score, con_score, int_score, wis_score, cha_score):
    # check to see if the character already exists in the database
    result = None
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string
        query = "SELECT * FROM chars WHERE character_name = ? AND user_id = ?"
        # execute our query
        cursor.execute(query, name, user_id)
        # use cursor to fetch the results of the query
        result = cursor.fetchone()
    finally:
        # close our database connection
        connection.close()

    if result is not None:
        print("Character: " + name + " - Is Already In Database")
        return str("Character: " + name + " - Is Already In Database")

    print("Adding Character: " + name)
    # create a character object
    new_character = Character(name, str_score, dex_score, con_score, int_score, wis_score, cha_score, user_id)
    # call the dao method
    return dao.create_character(new_character)


def get_character(index):
    db_character = dao.get_character(index)
    return Character(db_character[1], db_character[3], db_character[4], db_character[5], db_character[6],
                     db_character[7], db_character[8], db_character[2])

