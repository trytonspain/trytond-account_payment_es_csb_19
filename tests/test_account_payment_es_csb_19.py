# This file is part of the account_payment_es_csb_19 module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class AccountPaymentEsCsb19TestCase(ModuleTestCase):
    'Test Account Payment Es Csb 19 module'
    module = 'account_payment_es_csb_19'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        AccountPaymentEsCsb19TestCase))
    return suite