__author__ = 'Dan'
"""
#-------------------------------------------------------------------------------
# Name:        CarObject
# Purpose:
#
# Author:      Dan
#
# Created:     03.11.2012
# Copyright:   ( c ) Dan 2012
# Usage:
        dictionary = {"Producator":"Mercedes","Caroserie":"Sedan","Model":"C180","AnProductie":1999,"VolumMotor":1800,
                      "Pret":8000,"Carburant":"Benzina","Link":"http://www.google.ro"}
        object = CarObject.carObject(dictionary)

#-------------------------------------------------------------------------------
"""
class CarObject:
    def __init__(self,dict):
        self._Caroserie = dict['Caroserie']
        self._Producator = dict['Producator']
        self._Model = dict['Model']
        self._AnProductie = dict['AnProductie']
        self._VolumMotor =  dict['VolumMotor']
        self._Pret  = dict['Pret']
        self._Carburant = dict['Carburant']
        self._Link = dict['Link']