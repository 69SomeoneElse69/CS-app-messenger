"""Unit-тесты клиента"""

import sys
import os
import unittest
sys.path.append(os.path.join(os.getcwd(), '..'))
from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from client import is_client_here, server_answer_in


class TestClass(unittest.TestCase):
    '''
    Класс с тестами
    '''

    def test_def_presense(self):
        """Тест коректного запроса"""
        test = is_client_here()
        test[TIME] = 1.1  # время необходимо приравнять принудительно
                          # иначе тест никогда не будет пройден
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_200_ans(self):
        """Тест корректтного разбора ответа 200"""
        self.assertEqual(server_answer_in({RESPONSE: 200}), '200 : OK')

    def test_400_ans(self):
        """Тест корректного разбора 400"""
        self.assertEqual(server_answer_in({RESPONSE: 400, ERROR: 'Bad Request'}), '400 : Bad Request')

    def test_no_response(self):
        """Тест исключения без поля RESPONSE"""
        self.assertRaises(ValueError, server_answer_in, {ERROR: 'Bad Request'})


if __name__ == '__main__':
    unittest.main()
