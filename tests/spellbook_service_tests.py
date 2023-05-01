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
        dao.get_spellbook = Mock(side_effect=self.args_based_return)
        #dao.get_spellbook = Mock(return_value=(1, 1, 'UserID-CharacterName-Class', 'wizard', 1))
        dao.get_spellbook_spells = Mock(side_effect=self.args_based_return_spells)
        #dao.get_spellbook_spells = Mock(return_value=[(1, 1, 'acid-splash'), (2, 1, 'mage-hand'),
                 #                                     (3, 1, 'chill-touch')])
        dao.get_spellbook_spell = Mock(side_effect=self.args_based_return)
        #dao.get_spellbook_spell = Mock(return_value=(1, 1, 'acid-splash'))
        dao.get_user = Mock(side_effect=self.args_based_return)
        dao.get_character = Mock(side_effect=self.args_based_return)

    # test the create spellbook function
    def test_create_spellbook(self):
        # execute the function without a spellbook ID and with an invalid user id
        result = service.create_spellbook(3, 3, 'wizard', 1)
        # assert that the dao create spellbook function was not called
        dao.create_spellbook.assert_not_called()
        # assert that the service function returned the correct error message
        assert result == "That user does not exist"

        # execute the function without a spellbook ID and with an invalid character id
        result = service.create_spellbook(2, 2, 'wizard', 1)
        # assert that the dao create spellbook function was not called
        dao.create_spellbook.assert_not_called()
        # assert that the service function returned the correct error message
        assert result == "That spellbook already exists"

        # execute the function without a spellbook ID and with an invalid class
        result = service.create_spellbook(2, 3, 'Wizard', 1)
        # assert that the dao create spellbook function was not called
        dao.create_spellbook.assert_not_called()
        # assert that the service function returned the correct error message
        assert result == "That class does not exist"

        # execute the function without a spellbook ID and with a class level that is too low
        result = service.create_spellbook(2, 3, 'wizard', 0)
        # assert that the dao create spellbook function was not called
        dao.create_spellbook.assert_not_called()
        # assert that the service function returned the correct error message
        assert result == "That spellcasting level is invalid"

        # execute the function without a spellbook ID and with a class level that is too high
        result = service.create_spellbook(2, 3, 'wizard', 21)
        # assert that the dao create spellbook function was not called
        dao.create_spellbook.assert_not_called()
        # assert that the service function returned the correct error message
        assert result == "That spellcasting level is invalid"

        # execute the function without a spellbook ID
        result = service.create_spellbook(2, 3, 'wizard', 1)
        # assert that the dao create spellbook function was called with the correct parameters
        dao.create_spellbook.assert_called_with(2, 3, 'wizard', 1, 'default')
        # assert that the service function returned a null value
        assert result is None

        # execute the function with a spellbook ID
        result = service.create_spellbook(2, 3, 'wizard', 1, 1)
        # assert that the dao create spellbook function was called with the correct parameters
        dao.create_spellbook.assert_called_with(2, 3, 'wizard', 1, 1)
        # assert that the service function returned a null value
        assert result is None

    # test the delete spellbook function
    def test_delete_spellbook(self):
        # execute the function with an invalid spellbook id
        result = service.delete_spellbook(3)
        # assert that the dao delete spellbook function was not called
        dao.delete_spellbook.assert_not_called()
        # assert that the service function returned the correct error message
        assert result == "That spellbook does not exist"

        # execute the function with a valid spellbook ID
        result = service.delete_spellbook(2)
        # assert that the dao delete spellbook function was called with the correct parameters
        dao.delete_spellbook.assert_called_with(2)
        # assert that the service function returned a null value
        assert result is None

    # test the get spellbook function
    def test_get_spellbook(self):
        # execute the function with an invalid spellbook ID
        result = service.get_spellbook(3)
        # assert that the dao get spellbook function was called with the correct parameters
        dao.get_spellbook.assert_called_with(3)
        # assert that the dao get spellbook spells function was not called
        dao.get_spellbook_spells.assert_not_called()
        # assert that the service function returned a null value
        assert result is None

        # execute the function with a valid spellbook ID
        result = service.get_spellbook(1)
        # assert that the dao get spellbook function was called with the correct parameters
        dao.get_spellbook.assert_called_with(1)
        # assert that the dao get spellbook spells function was called with the correct parameters
        dao.get_spellbook_spells.assert_called_with(1)
        # assert that the service function returned a spellbook object with all the correct values
        assert result.__class__ == SpellBook
        assert result.get_spellbook_id() == 1
        assert result.get_user_id() == 1
        assert result.get_character_id() == 'UserID-CharacterName-Class'
        assert result.get_spell_casting_class() == 'wizard'
        assert result.get_spell_casting_level() == 1
        assert result.get_spells() == 'acid-splash,mage-hand,chill-touch'

    def args_based_return(*args, **kwargs):
        if args.__contains__(1):
            return 1, 1, 'UserID-CharacterName-Class', 'wizard', 1
        elif args.__contains__(2):
            return 2
        elif args.__contains__(3):
            return None
        else:
            return Exception("exception occurred")

    def args_based_return_spells(*args, **kwargs):
        if args.__contains__(1):
            return [(1, 1, 'acid-splash'), (2, 1, 'mage-hand'),(3, 1, 'chill-touch')]
        elif args.__contains__(2):
            return None
        else:
            return Exception("exception occurred")
