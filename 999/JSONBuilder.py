#-------------------------------------------------------------------------------
# Name:        JSON Builder
# Purpose:     Builds a JSON string
#
# Author:      Vlad
#
# Created:     03.11.2012
# Copyright:   (c) Vlad 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import string
from CarObject import CarObject

class JSONBuilder(object):
  """
  returns a json string from an array of car objects
  """
  @staticmethod
  def getJSON(cars):
    jsonObjects = []
    for car in cars:
      jsonObject = JSONObject(car)
      jsonObjects.append(jsonObject)

    jsonString = JSONBuilder.buildJSON(jsonObjects)
    jsonString = JSONBuilder.beautifierJSON(jsonString)
    return jsonString

  @staticmethod
  def buildJSON(objectsJSON):
    jsonString = ''
    i = 0

    for objectJSON in objectsJSON:
      jsonString += str(objectJSON)
      if i < len(objectsJSON) - 1:
        jsonString +=','
      i += 1

    return jsonString

  @staticmethod
  def beautifierJSON(jsonString):
    position = -1
    while 1:
      position = string.find(jsonString, '{', position+len("{"))
      if position == -1:
        break
      jsonString = jsonString[0:position+1] + "\r\n" + jsonString[position+1:]

    position = -1
    while 1:
      position = string.find(jsonString, '}', position+len("\r\n}"))
      if position == -1:
        break
      jsonString = jsonString[0:position] + "\r\n" + jsonString[position:]

    position = -1
    while 1:
      position = string.find(jsonString, ',', position+len("\r\n}"))
      if position == -1:
        break
      jsonString = jsonString[0:position+1] + "\r\n" + jsonString[position+1:]


    lines = jsonString.splitlines(True)
    jsonString = ''
    for line in lines:
      if line[0] == '"':
        line = "  " + line
      jsonString += line

    return "[" + jsonString + "]"



class JSONObject(object):
  """
  represents a single JSON Object,
  all the fields are stored into an array
  """
  def __init__(self, car):
    self.fields = []

    for property, value in vars(car).iteritems():
      property = property[1:]
      field = Field(property, value)
      self.fields.append(field)

  def __str__(self):
    """
    returns a JSON string from the JSON Object
    """
    jsonString = ''
    i = 0

    for field in self.fields:
      jsonString += str(field)
      if i < len(self.fields) - 1:
        jsonString += ','
      i += 1

    jsonString = '{' + jsonString + '}'
    return jsonString



class Field(object):
  """
  represents a key:value pair
  """
  def __init__(self, fieldKey = None, fieldValue = None):
    self.key = FieldKey(fieldKey)
    self.value = FieldValue(fieldValue)

  def __str__(self):
    return (str(self.key) + ':' + str(self.value))



class FieldKey(object):
  """
  key field from the key:value pair
  """
  def __init__(self, value = None):
    self.__dict__['_value'] = value

  def __getattr__(self):
    return self.__str__()

  def __str__(self):
    if self.__dict__['_value'] == None:
      return ''
    else:
      return '"' + self.__dict__['_value'] + '"'

  def setKey(self, value):
    self._value = value



class FieldValue(object):
  """
  value field from the key:value pair
  """
  def __init__(self, value = None):
    self.__dict__['_value'] = value

  def __getattr__(self):
    return self.__str__()

  def __str__(self):
    if self.__dict__['_value'] == None:
      return ''
    if isinstance(self.__dict__['_value'], str):
      return '"' + self.__dict__['_value'] + '"'
    if isinstance(self.__dict__['_value'], int):
      return str(self.__dict__['_value'])

  def setValue(self, value):
    self._value = value



"""
#JSONBuilder.BuildJSON(["BMW", "M3"])
cars = []
dictionary = {"Producator":"Mercedes","Caroserie":"Sedan","Model":"C180","AnProductie":1999,"VolumMotor":1800,
                      "Pret":8000,"Carburant":"Benzina","Link":"http://www.google.ro"}
car = CarObject(dictionary)
cars.append(car)

dictionary = {"Producator":"BMW","Caroserie":"Sedan","Model":"M3","AnProductie":1999,"VolumMotor":1800,
                      "Pret":8000,"Carburant":"Diesel","Link":"http://www.google.ro"}
car = CarObject(dictionary)
cars.append(car)


print JSONBuilder.getJSON(cars)
"""