from src.app import app, request, session, redirect

# import our service level logic for reimbursements
import src.service.character_service as service

# import json formatting logic
from src.models.character import CharacterEncoder
from json import dumps


@app.route('/characters/<string:character_index>', methods=['GET'])
def get_character(character_index):
    # use service layer logic to get results
    result = service.get_character(character_index)
    result = dumps(result, cls=CharacterEncoder)

    # return the result in json form
    return result, 200


@app.route('/characters', methods=['POST'])
def create_character():
    character_data = request.json
    result = service.create_character(character_data['name'], character_data['user_id'], character_data['str_score'],
                                      character_data['dex_score'], character_data['con_score'],
                                      character_data['int_score'], character_data['wis_score'],
                                      character_data['cha_score'])
    return result, 200
