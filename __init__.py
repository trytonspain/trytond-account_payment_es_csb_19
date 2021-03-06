# This file is part of account_payment_es_csb_19 module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .payment import *


def register():
    Pool.register(
        Journal,
        Group,
        module='account_payment_es_csb_19', type_='model')
