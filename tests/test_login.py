from odoo.tests import TransactionCase
from .. helpers import string
import logging

_logger = logging.getLogger(__name__)

class LoginTesting(TransactionCase):
    def test_login_exist(self):
        self.assertTrue('rest.log' in self.env)
        _logger.info("**************************************")  

    