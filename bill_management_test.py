# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 19:25:38 2019

@author: clintonngan
"""
import unittest

from bill_management import read_bills

class TestBillManagement(unittest.TestCase):
    
    def test_read_bills(self):
        bills = read_bills()
        self.assertEqual(33, len(bills))
        self.assertEqual('Electric Ireland', bills[1][0])
        self.assertEqual('credit', bills[20][6])
        self.assertEqual('credit', bills[23][6])
        
    def test_write_bills(self):
        bills = read_bills()
        bills = read_bills()
        self.assertEqual(33, len(bills))
        self.assertEqual('Electric Ireland', bills[1][0])
        self.assertEqual('credit', bills[20][6])
        
if __name__ == '__main__':
    unittest.main()