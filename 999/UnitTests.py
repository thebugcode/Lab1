#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Vlad
#
# Created:     03.11.2012
# Copyright:   (c) Vlad 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import unittest
from JSONBuilder import JSONBuilder

class JSONBuilderTest(unittest.TestCase):
  def testSum(self):
    builder = JSONBuilder()
    builder.sumAB(2,3)
    self.assertEqual(builder.sum, 5)

if __name__ == '__main__':
  unittest.main()