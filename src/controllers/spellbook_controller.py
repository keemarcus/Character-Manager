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


@app.route('/reimbursements', methods=['POST'])
def create_spellbook():
    employee_id = session.get('user_id')
    amount = request.form.get('amount')
    reason = request.form.get('reason')
    date = datetime.datetime.now().replace(microsecond=0)

    # call service function to create new reimbursement
    service.create_reimbursement(employee_id, amount, reason, date)

    # log creation of new reimbursement
    reimbursement_logger.info(f"""Created new reimbursement for user: {employee_id}, 
                                  Amount: {amount}, Reason: {reason}, 
                                  Created: {date}.""")

    # send the user to the reimbursements page
    return redirect('http://localhost:5000/reimbursements.html')


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
