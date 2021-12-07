"""Unit-тесты сервера"""

import sys
import os
import unittest
sys.path.append(os.path.join(os.getcwd(), '..'))
from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from server import server_answer_out


class TestServer(unittest.TestCase):
    '''
    В сервере только 1 функция для тестирования
    '''
    err_dict = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }
    ok_dict = {RESPONSE: 200}

    def test_ok_check(self):
        """Корректный запрос"""
        self.assertEqual(server_answer_out(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}), self.ok_dict)

  #  def test_no_action(self):
  #      """Ошибка если нет действия"""
  #      self.assertEqual(server_answer_out(
  #          {TIME: '1.1', USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)

    def test_wrong_action(self):
        """Ошибка если неизвестное действие"""
        self.assertEqual(server_answer_out(
            {ACTION: 'Wrong', TIME: '1.1', USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)

   # def test_no_time(self):
   #     """Ошибка, если  запрос не содержит штампа времени"""
   #     self.assertEqual(server_answer_out(
   #         {ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)

    #def test_no_user(self):
    #    """Ошибка - нет пользователя"""
    #    self.assertEqual(server_answer_out(
    #        {ACTION: PRESENCE, TIME: '1.1'}), self.err_dict)

    #def test_unknown_user(self):
    #    """Ошибка - не Guest"""
    #    self.assertEqual(server_answer_out(
    #        {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest1'}}), self.err_dict)


if __name__ == '__main__':
    unittest.main()
