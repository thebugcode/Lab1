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
from CarObject import CarObject

class CarObjectTest(unittest.TestCase):
  aDictionary = { "Producator":"Mercedes","Caroserie":"Sedan","Model":"C180",
                  "AnProductie":1999,"VolumMotor":1800,"Pret":8000,
                  "Carburant":"Benzina","Link":"http://www.google.ro"}
  car = CarObject(aDictionary)
  self.assertEqual(car._AnProductie, 1999)
  self.assertEqual(car._Carburant, Benzina)
  self.assertEqual(car._Pret, 8000)


class JSONBuilderTest(unittest.TestCase):
  def testSum(self):
    cars = []
    aDictionary = { "Producator":"Mercedes","Caroserie":"Sedan","Model":"C180",
                    "AnProductie":1999,"VolumMotor":1800,"Pret":8000,
                    "Carburant":"Benzina","Link":"http://www.google.ro" }
    car = CarObject(aDictionary)
    cars.append(car)

    aDictionary = { "Producator":"BMW","Caroserie":"Sedan","Model":"M3",
                    "AnProductie":1999,"VolumMotor":1800,"Pret":8000,
                    "Carburant":"Diesel","Link":"http://www.google.ro" }
    car = CarObject(dictionary)
    cars.append(car)

    print JSONBuilder.getJSON(cars)

if __name__ == '__main__':
  unittest.main()