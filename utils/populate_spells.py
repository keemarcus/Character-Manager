import requests
from src.models.spell import Spell
import src.service.spell_service as service
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
                  'subclasses': None,
                  'user_id': 0}

    spell_info = requests.get("https://www.dnd5eapi.co/api/spells/" + spell["index"]).json()
    for field in spell_info:
        if field in ['classes', 'subclasses']:
            data = ""
            for entry in spell_info[field]:
                data += entry["index"] + " - "
            spell_data[field] = data[:-3]
        elif field in ['higher_level', 'desc']:
            if len(str(spell_info[field])) == 2:
                spell_data[field] = None
            else:
                spell_data[field] = str(spell_info[field]).replace('["', '').replace("']", '').replace('"]', '')\
                    .replace("['", '').replace(", '", ', "')
        elif field == 'components':
            spell_data[field] = str(spell_info[field]).replace('[', '').replace(']', '').replace("'", '')
        elif field == 'school':
            spell_data[field] = spell_info[field]['index']
        else:
            spell_data[field] = str(spell_info[field])

    service.create_spell(spell_data['index'], spell_data['user_id'], spell_data['name'], spell_data['level'],
                         spell_data['classes'], spell_data['subclasses'], spell_data['school'],
                         spell_data['casting_time'], spell_data['range'], spell_data['duration'],
                         spell_data['components'], spell_data['material'], spell_data['concentration'],
                         spell_data['desc'], spell_data['ritual'], spell_data['dc'], spell_data['higher_level'],
                         spell_data['damage'], spell_data['area_of_effect'], spell_data['heal_at_slot_level'],
                         spell_data['attack_type'])

print("Number of Spells: " + spell_count.__str__())
