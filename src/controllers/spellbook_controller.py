# import our flask app and database connection/cursor from app.py
import datetime

from src.app import app, request, session, redirect

# import our service level logic for reimbursements
import src.service.spellbook_service as service

# import json formatting logic
from src.models.spellbook import SpellbookEncoder
from json import dumps

# set up logging
import logging


@app.route('/spellbooks/restore/<int:spellbook_id>', methods=['POST'])
def restore_spell_slots(spellbook_id):
    result = service.restore_spell_slots(spellbook_id)
    result = dumps(result, cls=SpellbookEncoder)

    # return the result in json form
    return result, 200


@app.route('/spellbooks/cast', methods=['POST'])
def cast_spell():
    spellbook_id = request.form.get('spellbook_id')
    character_id = str(request.form.get('character_id'))
    spell_index = str(request.form.get('spell_index'))
    spell_level = int(request.form.get('spell_level'))

    # return the result in json form
    result = service.cast_spell(character_id, spellbook_id, spell_index, spell_level)
    return result


@app.route('/spellbooks', methods=['POST'])
def create_spellbook():
    spellbook_id = request.form.get('spellbook_id')
    user_id = int(request.form.get('user_id'))
    character_id = str(request.form.get('character_id'))
    spell_casting_class = str(request.form.get('spell_casting_class'))
    spell_casting_level = int(request.form.get('spell_casting_level'))
    # date = datetime.datetime.now().replace(microsecond=0)

    # call service function to create new reimbursement
    if spellbook_id is None or spellbook_id == "":
        result = service.create_spellbook(user_id, character_id, spell_casting_class, spell_casting_level)
    else:
        result = service.create_spellbook(user_id, character_id, spell_casting_class, spell_casting_level, spellbook_id)

    # return the result in json form
    result = dumps(result, cls=SpellbookEncoder)
    return result, 200

    # send the user to the reimbursements page
    return redirect('http://localhost:5000/reimbursements.html')


@app.route('/spellbooks/<int:spellbook_id>', methods=['DELETE'])
def delete_spellbook(spellbook_id):
    # call service function to create new reimbursement
    result = service.delete_spellbook(spellbook_id)

    # return the result in json form
    result = dumps(result, cls=SpellbookEncoder)
    return result, 200


@app.route('/spellbooks/<int:spellbook_id>', methods=['PATCH'])
def update_spellbook(spellbook_id):
    user_id = int(request.form.get('user_id'))
    character_id = str(request.form.get('character_id'))
    spell_casting_class = str(request.form.get('spell_casting_class'))
    spell_casting_level = int(request.form.get('spell_casting_level'))

    # call service function to create new reimbursement
    result = service.update_spellbook(spellbook_id, user_id, character_id, spell_casting_class, spell_casting_level)

    # return the result in json form
    result = dumps(result, cls=SpellbookEncoder)
    return result, 200


@app.route('/spellbooks/<int:spellbook_id>', methods=['GET'])
def get_spellbook(spellbook_id):
    # use service layer logic to get results
    result = service.get_spellbook(spellbook_id)
    result = dumps(result, cls=SpellbookEncoder)

    # return the result in json form
    return result, 200


@app.route('/spellbooks/<int:spellbook_id>/<string:spell_index>', methods=['POST'])
def add_spell(spellbook_id, spell_index):
    # use service layer logic to get results
    result = service.add_spell(spellbook_id, spell_index)
    result = dumps(result, cls=SpellbookEncoder)

    # return the result in json form
    return result, 200


@app.route('/spellbooks/<int:spellbook_id>/<string:spell_index>', methods=['DELETE'])
def delete_spell(spellbook_id, spell_index):
    # use service layer logic to get results
    result = service.delete_spell(spellbook_id, spell_index)
    result = dumps(result, cls=SpellbookEncoder)

    # return the result in json form
    return result, 200


@app.route('/spellbooks/spells/<int:spellbook_id>', methods=['GET'])
def get_spellbook_spells(spellbook_id):
    print(spellbook_id)
    # use service layer logic to get results
    result = service.get_spellbook_spells(spellbook_id)

    # return the result in json form
    return result, 200


@app.route('/reimbursements/<int:reimbursement_id>', methods=['POST'])
def update_reimbursement(reimbursement_id):
    # get data from request form
    amount = request.form.get('amount')
    reason = request.form.get('reason')
    date = datetime.datetime.now().replace(microsecond=0)

    # use service layer logic to update the reimbursement
    service.update_reimbursement(reimbursement_id, amount, reason, date)

    # log update of reimbursement
    reimbursement_logger.info(f"""Updated reimbursement with ID: {reimbursement_id}, 
                                      Amount: {amount}, Reason: {reason}, 
                                      Updated: {date}.""")

    # return the user to the page they were just on
    return redirect(request.referrer)
