# import our get connection function
from utils import dbconfig


# add a new spell to the database
def create_spell(index, name, desc, spell_range, components, duration, concentration, casting_time, level, school,
                 classes, subclasses, dc, higher_level, ritual, damage, attack_type):
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string using parameterization to protect against SQL injection
        query = "INSERT INTO spells VALUES (default, ?, ?, ?, ?, ?, ?, ?, ?)"
        # execute our query and commit the changes to the database
        cursor.execute(query, index, name, desc, spell_range, components, duration, concentration, casting_time, level,
                       school, classes, subclasses, dc, higher_level, ritual, damage, attack_type)
        cursor.commit()
    finally:
        # close our database connection
        connection.close()


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
