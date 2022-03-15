from odoo.tests import TransactionCase
from odoo.tests import common
import unittest
import logging

_logger = logging.getLogger(__name__)

class TestModule(common.TransactionCase):
    def setUp(self):
        super(TestModule, self).setUp()

    def test_data(self):
        test_staff = self.env['rest.staff'].create({
            'full_name': 'Odoo Developer',
            'age': 25,
            'mobile': '01761970239',
            'email': 'azharulamin.cse@gmail.com'
        })

        test_ctc = self.env['rest.staff'].create({
            'hand_salary': 15000,
            'epf_esi': 5000,
        })
        print(test_staff, test_ctc+"Staff created")

    def test_limitation(self):
        hand_salary_status = self.env['rest.staff'].search(
            [('hand_salary', '<', 5000)])
        for rec in hand_salary_status:
            _logger.info("The result is",hand_salary_status.hand_salary)
            _logger.info("------------------------")
            print("Full Name:############", rec.full_name,
                  'gender: $$$$$$$$$$', rec.gender)
            
        _logger.warning( rec.full_name, rec.gender,"Unable to access the attachments of %s. Tried to decrypt it, but %s.")
           


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('full_name'.upper())


class TestAge(unittest.TestCase):
    def test_age(self):
        self.env['rest.staff'].val_age()
        self.assertAlmostEqual(self.test_age(19))
        self.assertRaises(self.test_age(
            10), expected_exception="Age should greater then 18")
