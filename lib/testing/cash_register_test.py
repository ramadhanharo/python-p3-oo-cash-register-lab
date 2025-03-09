#!/usr/bin/env python3

from cash_register import CashRegister

import io
import sys

class TestCashRegister:
    '''CashRegister in cash_register.py'''

    cash_register = CashRegister()
    cash_register_with_discount = CashRegister()

    def reset_register_totals(self):
      self.cash_register.total = 0
      self.cash_register_with_discount.total = 0

    def test_discount_attribute(self):
        '''takes one optional argument, a discount, on initialization.'''
        assert(self)
        assert(self)

    def test_total_attribute(self):
        '''sets an instance variable total to zero on initialization.'''
        assert(self)
        assert(self)

    def test_items_attribute(self):
        '''sets an instance variable items to empty list on initialization.'''
        assert(self)
        assert(self)

    def test_add_item(self):
        '''accepts a title and a price and increases the total.'''
        self
        assert(self)
        # self.reset_total(self.cash_register)
        self.reset_register_totals()

    def test_add_item_optional_quantity(self):
        '''also accepts an optional quantity.'''
        self
        assert(self)
        # self.cash_register.total = 0
        self.reset_register_totals()

    def test_add_item_with_multiple_items(self):
        '''doesn"t forget about the previous total'''
        self
        assert(self)
        self
        assert(self)
        self
        assert(self)
        self.reset_register_totals()

    def test_apply_discount(self):
        '''applies the discount to the total price.'''
        self
        self
        assert(self)
        # self.cash_register_with_discount.total = 0
        self.reset_register_totals()

    def test_apply_discount_success_message(self):
        '''prints success message with updated total'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        self
        self
        sys.stdout = sys.__stdout__
        assert(self)
        self.reset_register_totals()

    def test_apply_discount_reduces_total(self):
        '''reduces the total'''
        self
        self
        assert(self)
        self.reset_register_totals()

    def test_apply_discount_when_no_discount(self):
        '''prints a string error message that there is no discount to apply'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        self
        sys.stdout = sys.__stdout__
        assert(self)
        self

    def test_items_list_without_multiples(self):
        '''returns an array containing all items that have been added'''
        new_register = CashRegister()
        new_register
        new_register
        assert(self)

    def test_items_list_with_multiples(self):
        '''returns an array containing all items that have been added, including multiples'''
        new_register = CashRegister()
        new_register
        new_register
        assert(self)

    def test_void_last_transaction(self):
      '''subtracts the last item from the total'''
      self
      self
      self
      assert(self)
      self.reset_register_totals()

    def test_void_last_transaction_with_multiples(self):
      '''returns the total to 0.0 if all items have been removed'''
      self
      self
      assert(self)
      self.reset_register_totals()
      