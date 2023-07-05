from utils import dbconfig
import requests
from src.models.spell import Spell
import json

spell_count = 0

spells = requests.get("https://www.dnd5eapi.co/api/spells").json()
for spell in spells["results"]:
    spell_count += 1
    # spell_data = {'casting_time': None,
    #               'attack_type': None,
    #               'range': None,
    #               'duration': None,
    #               'components': None,
    #               'damage': None,
    #               'dc': None,
    #               'higher_level': None,
    #               'ritual': None,
    #               'classes': None,
    #               'name': None,
    #               'school': None,
    #               'area_of_effect': None,
    #               'heal_at_slot_level': None,
    #               'desc': None,
    #               'concentration': None,
    #               'level': None,
    #               'material': None,
    #               'index': None,
    #               'subclasses': None}
    spell_datax = Spell(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                        None, None, None, None, None)
    spell_info = requests.get("https://www.dnd5eapi.co/api/spells/" + spell["index"]).json()
    for field in spell_info:
        if field == 'index':
            spell_datax.set_index(str(spell_info[field]))
        elif field == 'name':
            spell_datax.set_name(str(spell_info[field]))
        elif field == 'level':
            spell_datax.set_level(str(spell_info[field]))
        elif field == 'classes':
            data = ""
            for entry in spell_info[field]:
                data += entry["index"] + " - "
            spell_datax.set_classes(data[:-3])
        elif field == 'subclasses':
            data = ""
            for entry in spell_info[field]:
                data += entry["index"] + " - "
            spell_datax.set_subclasses(data[:-3])
        elif field == 'school':
            spell_datax.set_school(spell_info[field]['index'])
        elif field == 'casting_time':
            spell_datax.set_casting_time(str(spell_info[field]))
        elif field == 'range':
            spell_datax.set_range(str(spell_info[field]))
        elif field == 'duration':
            spell_datax.set_duration(str(spell_info[field]))
        elif field == 'components':
            spell_datax.set_components(str(spell_info[field]))
        elif field == 'materials':
            spell_datax.set_materials(str(spell_info[field]))
        elif field == 'concentration':
            spell_datax.set_concentration(str(spell_info[field]))
        elif field == 'desc':
            spell_datax.set_desc(str(spell_info[field]))
        elif field == 'ritual':
            spell_datax.set_ritual(str(spell_info[field]))
        elif field == 'dc':
            spell_datax.set_dc(str(spell_info[field]))
        elif field == 'higher_level':
            spell_datax.set_higher_level(str(spell_info[field]))
        elif field == 'damage':
            spell_datax.set_damage(str(spell_info[field]))
        elif field == 'area_of_effect':
            spell_datax.set_area_of_effect(str(spell_info[field]))
        elif field == 'heal_at_slot_level':
            spell_datax.set_heal_at_slot_level(str(spell_info[field]))
        else:
            spell_datax.set_attack_type(str(spell_info[field]))

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
        print("Adding Spell: " + spell_datax.get_name())
        try:
            # set up a new database connection and cursor
            connection = dbconfig.get_connection()
            cursor = connection.cursor()
            # create query string using parameterization to protect against SQL injection
            query = "INSERT INTO spells VALUES (?, 0, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            # execute our query and commit the changes to the database
            cursor.execute(query, spell_datax.get_index(), spell_datax.get_name(), spell_datax.get_level(), spell_datax.get_classes(),
                           spell_datax.get_subclasses(), spell_datax.get_school(), spell_datax.get_casting_time(),
                           spell_datax.get_range(), spell_datax.get_duration(), spell_datax.get_components(),
                           spell_datax.get_material(), spell_datax.get_concentration(), spell_datax.get_desc(),
                           spell_datax.get_ritual(), spell_datax.get_dc(), spell_datax.get_higher_level(), spell_datax.get_damage(),
                           spell_datax.get_area_of_effect(), spell_datax.get_heal_at_slot_level(), spell_datax.get_attack_type())
            cursor.commit()
        finally:
            # close our database connection
            connection.close()
    else:
        print("Spell: " + spell_datax.get_name() + " - Is Already In Database")

print("Number of Spells: " + spell_count.__str__())
