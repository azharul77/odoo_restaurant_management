# from odoo.addons.resturant_project.helpers import posting
from odoo.tests import TransactionCase
from odoo.exceptions import ValidationError
from ..helpers import posting
import logging

_logger = logging.getLogger(__name__)

class PostHelperTest(TransactionCase):
    def setUp(self):
        super(PostHelperTest, self).setUp()
   

        self.login = self.env['rest.log'].create({'username': 'my_username', 'password': 'my_password'})
        self.posting = posting.Post(self.login)

        def test_posting_create_post_with_valid_data(self):
            post = self.posting.post(description="This food is so good.")
            self.assertTrue(bool(self.env['rest.post'].search([('id', '=', post.id)], limit=1)))
            _logger.info(test_posting_create_post_with_valid_data)

        def test_posting_create_post_throws_exception_with_invalid_data(self):
            with self.assertRaises(ValidationError):
                self.posting.post(description='=' * 150)    