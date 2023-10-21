from app import app, request, session, redirect

# import our service level logic for reimbursements
import src.service.spell_service as service

# import json formatting logic
from src.models.spell import SpellEncoder
from json import dumps


@app.route('/new-spell/<int:user_id>', methods=['GET'])
def serve_add_spell_page(user_id):
    session['user_id'] = user_id
    return redirect('../add_spell.html')


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
    spell_index = request.form.get('name').strip().replace(' ', '-').lower()

    if request.form.get('level') == "cantrip":
        spell_level = 0
    else:
        spell_level = int(request.form.get('level'))


    spell_classes = ""
    for spell_class in request.form.getlist('classes'):
        spell_classes = spell_classes + spell_class + " - "
    if len(spell_classes) > 0:
        spell_classes = spell_classes[:-3]
    else:
        spell_classes = None

    spell_subclasses = ""
    for spell_subclass in request.form.getlist('subclasses'):
        spell_subclasses = spell_subclasses + spell_subclass + " - "
    if len(spell_subclasses) > 0:
        spell_subclasses = spell_subclasses[:-3]
    else:
        spell_subclasses = None

    spell_components = ""
    for spell_component in request.form.getlist('components'):
        spell_components = spell_components + spell_component + ", "
    if len(spell_components) > 0:
        spell_components = spell_components[:-2]
    else:
        spell_components = None

    concentration = "False"
    if request.form.get('concentration') is not None:
        concentration = "True"

    ritual = "False"
    if request.form.get('ritual') is not None:
        ritual = "True"

    result = service.create_spell(
        spell_index,
        request.form.get('user_id'),
        request.form.get('name'),
        spell_level,
        spell_classes,
        spell_subclasses,
        request.form.get('school'),
        request.form.get('casting_time'),
        request.form.get('range'),
        request.form.get('duration'),
        spell_components,
        request.form.get('material'),
        concentration,
        request.form.get('desc'),
        ritual,
        request.form.get('dc'),
        request.form.get('higher_level'),
        request.form.get('damage'),
        request.form.get('area_of_effect'),
        request.form.get('heal_at_slot_level'),
        request.form.get('attack_type'))

    return result, 200
