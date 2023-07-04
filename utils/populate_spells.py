from utils import dbconfig
import requests
import json

spell_count = 0

spells = requests.get("https://www.dnd5eapi.co/api/spells").json()
for spell in spells["results"]:
    spell_count += 1
    spell_data = {'casting_time': None,
                  'attack_type': None,
                  'range': None,
                  'duration': None,
                  'components': None,
                  'damage': None,
                  'dc': None,
                  'higher_level': None,
                  'ritual': None,
                  'classes': None,
                  'name': None,
                  'school': None,
                  'area_of_effect': None,
                  'heal_at_slot_level': None,
                  'desc': None,
                  'concentration': None,
                  'level': None,
                  'material': None,
                  'index': None,
                  'subclasses': None}
    spell_info = requests.get("https://www.dnd5eapi.co/api/spells/" + spell["index"]).json()
    for field in spell_info:
        if field in ['classes', 'subclasses']:
            data = ""
            for entry in spell_info[field]:
                data += entry["index"] + " - "
            spell_data[field] = data[:-3]
        elif field == 'school':
            spell_data[field] = spell_info[field]['index']
        else:
            spell_data[field] = str(spell_info[field])

    # create result variable
    result = None
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string
        query = "SELECT * FROM spells WHERE spell_index = ?"
        # execute our query
        cursor.execute(query, spell_info['index'])
        # use cursor to fetch the results of the query
        result = cursor.fetchone()
    finally:
        # close our database connection
        connection.close()

    #print(result)
    if result is None:
        print("Adding Spell: " + spell_data['name'])
        try:
            # set up a new database connection and cursor
            connection = dbconfig.get_connection()
            cursor = connection.cursor()
            # create query string using parameterization to protect against SQL injection
            query = "INSERT INTO spells VALUES (?, 0, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            # execute our query and commit the changes to the database
            cursor.execute(query, spell_data['index'], spell_data['name'], spell_data['level'], spell_data['classes'],
                           spell_data['subclasses'], spell_data['school'], spell_data['casting_time'],
                           spell_data['range'], spell_data['duration'], spell_data['components'],
                           spell_data['material'], spell_data['concentration'], spell_data['desc'],
                           spell_data['ritual'], spell_data['dc'], spell_data['higher_level'], spell_data['damage'],
                           spell_data['area_of_effect'], spell_data['heal_at_slot_level'], spell_data['attack_type'])
            cursor.commit()
        finally:
            # close our database connection
            connection.close()
    else:
        print("Spell: " + spell_data['name'] + " - Is Already In Database")

print("Number of Spells: " + spell_count.__str__())
