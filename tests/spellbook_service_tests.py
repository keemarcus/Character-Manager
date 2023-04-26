import unittest
from unittest.mock import Mock

# import Spellbook class and spellbook_service module to be tested
from src.models.spellbook import SpellBook
from src.service import spellbook_service as service

# import our spellbook dao so that we can create a mock
from src.dao import spellbook_dao as dao


class SpellBookServiceTests(unittest.TestCase):
    def setUp(self):
        # create a mock so that when functions are called, mock values (stubs) are returned instead of real data
        dao.create_spellbook = Mock()
        dao.update_spellbook = Mock()
        dao.delete_spellbook = Mock()
        dao.add_spell = Mock()
        dao.delete_spell = Mock()
        dao.get_spellbook = Mock(return_value=(1, 1, 'UserID-CharacterName-Class', 'wizard', 1))
        dao.get_spellbook_spells = Mock(return_value=[(1, 1, 'acid-splash'), (2, 1, 'mage-hand'),
                                                      (3, 1, 'chill-touch')])
        dao.get_spellbook_spell = Mock(return_value=(1, 1, 'acid-splash'))
        dao.get_user = Mock(return_value=(2,))
        dao.get_character = Mock(return_value=None)

    # test our create spellbook function
    def test_create_spellbook(self):
        # execute the function without a spellbook ID
        service.create_spellbook(2, 2, 'wizard', 1)

        # assert that the dao create spellbook function was called with the correct parameters
        dao.create_spellbook.assert_called_with(2, 2, 'wizard', 1, 'default')

        # execute the function with a spellbook ID
        service.create_spellbook(2, 2, 'wizard', 1, 1)

        # assert that the dao create spellbook function was called with the correct parameters
        dao.create_spellbook.assert_called_with(2, 2, 'wizard', 1, 1)
