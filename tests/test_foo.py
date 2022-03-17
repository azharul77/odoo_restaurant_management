
# import odoo
from types import MethodDescriptorType
from odoo.tests import TransactionCase
from odoo.tests import common
'''most use's import function for testing '''
from odoo import api                                
# from odoo.sql_db import BaseCursor, Cursor
# from odoo.modules.registry import Registry
import unittest
import logging

# logger imported 
_logger = logging.getLogger(__name__)

# creating test class 
class TestModule(common.TransactionCase):

    # initialize setup method 
    def setUp(self):
        super(TestModule, self).setUp()

    # test method one created 
    def test_data(self):
        # creating new staff with minimum datas 
        test_staff = self.env['rest.staff'].create({
            'name': 'Odoo Developer',
            'age': 25,
            'mobile': '01761970239',
            'email': 'azharulamin.cse@gmail.com',
        })

        # checking etc operation 
        test_ctc = self.env['rest.staff'].create({
            'hand_salary': 15000,
            'epf_esi': 5000,
        })
        # added operations in logger method for visualizing the test methods results terminal interface 
        _logger.info("------------------------")
        _logger.info(test_staff)
        _logger.info(test_ctc)
        _logger.info("------------------------")

    # creating test method2
    # age goes throug conditonal helper 

    # @api.onchange('age')
    def test_age(self):
        age_cond = self.env['rest.staff'].search([('age', '>', '100'),])
        for rec in age_cond:
            print("&&&&&&&&&&&&&&&&&&",rec.name)
               
#  a practice testing method, have some issues,need to fix this.             

        # hand_salary_status = self.env['rest.staff'].search(
        #     [('hand_salary', '<', 5000)])
        # for rec in hand_salary_status:
        #     _logger.info("The result is",hand_salary_status.hand_salary)
        #     _logger.info("------------------------")
        #     print("Full Name:############", rec.name,
        #           'gender: $$$$$$$$$$', rec.gender)
              
        # _logger.warning( rec.name, rec.gender,"Unable to access the attachments of %s. Tried to decrypt it, but %s.")


# creating test class two 
class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('name'.upper())

# creating test class three 
class TestAge(unittest.TestCase):
    def setUp(self):
        super(TestAge, self).setUp()

# testing to check age verification
    
    def test_age(self):
        self.env['rest.staff'].val_age()
        self.assertAlmostEqual(self.test_age(13))
        self.assertRaises(self.test_age(
            10), expected_exception="Age should greater then 18")
