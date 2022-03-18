
# import warnings


# import odoo
# from odoo import api
# from odoo.modules.registry import Registry
# from odoo.sql_db import BaseCursor, Cursor
# from odoo.tests import BaseCase


# class TransactionCase(BaseCase):
#     registry: Registry = None
#     env: api.Environment = None
#     cr: Cursor = None

#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         cls.registry = odoo.registry(get_db_name())
#         cls.addClassCleanup(cls.registry.reset_changes)
#         cls.addClassCleanup(cls.registry.clear_caches)

#         cls.cr = cls.registry.cursor()
#         cls.addClassCleanup(cls.cr.close)

#         cls.env = api.Environment(cls.cr, odoo.SUPERUSER_ID, {})

#     def setUp(self):
#         super().setUp()

#         envs = self.env.all.envs
#         self.addCleanup(envs.update, list(envs))
#         self.addCleanup(envs.clear)

#         self.addCleanup(self.registry.clear_caches)
#         self.addCleanup(self.env.clear)

#         # flush everything in setUpClass before introducing a savepoint
#         self.env['base'].flush()

#         self._savepoint_id = next(savepoint_seq)
#         self.cr.execute('SAVEPOINT test_%d' % self._savepoint_id)
#         self.addCleanup(self.cr.execute, 'ROLLBACK TO SAVEPOINT test_%d' % self._savepoint_id)

#         self.patch(self.registry['res.partner'], '_get_gravatar_image', lambda *a: False)


# class SavepointCase(TransactionCase):
#     @classmethod
#     def __init_subclass__(cls):
#         super().__init_subclass__()
#         warnings.warn(
#             "Deprecated class SavepointCase has been merged into TransactionCase",
#             DeprecationWarning, stacklevel=2,
#         )



