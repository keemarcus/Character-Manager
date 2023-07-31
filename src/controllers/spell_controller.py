from src.app import app, request, session, redirect

# import our service level logic for reimbursements
import src.service.spell_service as service

# import json formatting logic
from src.models.spell import SpellEncoder
from json import dumps


@app.route('/spells/<string:spell_index>', methods=['GET'])
def get_spell(spell_index):
    # use service layer logic to get results
    result = service.get_spell(spell_index)
    result = dumps(result, cls=SpellEncoder)

    # return the result in json form
    return result, 200


@app.route('/spells/class/<string:class_name>', methods=['GET'])
def get_spells(class_name):
    # use service layer logic to get results
    result = service.get_spells(class_name)
    result = dumps(result, cls=SpellEncoder)

    # return the result in json form
    return result, 200


@app.route('/spells/class/<string:class_name>/level/<int:level>', methods=['GET'])
def get_spells_level(class_name, level):
    # use service layer logic to get results
    result = service.get_spells(class_name, None, level)
    result = dumps(result, cls=SpellEncoder)

    # return the result in json form
    return result, 200


@app.route('/spells/user/<int:user_id>/class/<string:class_name>/level/<int:level>', methods=['GET'])
def get_custom_spells_level(user_id, class_name, level):
    # use service layer logic to get results
    result = service.get_spells(class_name, user_id, level)
    result = dumps(result, cls=SpellEncoder)

    # return the result in json form
    return result, 200


@app.route('/spells', methods=['POST'])
def create_spell():
    # spell_data = request.json
    # result = service.create_spell(spell_data['index'], spell_data['user_id'], spell_data['name'], spell_data['level'],
    #                               spell_data['classes'], spell_data['subclasses'], spell_data['school'],
    #                               spell_data['casting_time'], spell_data['range'], spell_data['duration'],
    #                               spell_data['components'], spell_data['material'], spell_data['concentration'],
    #                               spell_data['desc'], spell_data['ritual'], spell_data['dc'],
    #                               spell_data['higher_level'],
    #                               spell_data['damage'], spell_data['area_of_effect'], spell_data['heal_at_slot_level'],
    #                               spell_data['attack_type'])

    result = service.create_spell(
        request.form.get('index'),
        request.form.get('user_id'),
        request.form.get('name'),
        request.form.get('level'),
        request.form.get('classes'),
        request.form.get('subclasses'),
        request.form.get('school'),
        request.form.get('casting_time'),
        request.form.get('range'),
        request.form.get('duration'),
        request.form.get('components'),
        request.form.get('material'),
        request.form.get('concentration'),
        request.form.get('desc'),
        request.form.get('ritual'),
        request.form.get('dc'),
        request.form.get('higher_level'),
        request.form.get('damage'),
        request.form.get('area_of_effect'),
        request.form.get('heal_at_slot_level'),
        request.form.get('attack_type'))

    return result, 200
