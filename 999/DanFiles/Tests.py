__author__ = 'Dan'
import unittest
import JSONBuilder
import DatabaseManager
import CarObject

###
class TestJson(unittest.TestCase):
    def test_JSON(self):
        json=JSONBuilder.JSONBuilder()
        object = json.buildJSON([1,5999])
        print object
        self.assertItemsEqual("{\"Pret\": 5999, \"ID\": 1}",object)
#test the CarObjectClass
class TestObject(unittest.TestCase):
    def test_OBJECT(self):
        dictionary = {"Producator":"Mercedes","Caroserie":"Sedan","Model":"C180","AnProductie":1999,"VolumMotor":1800,
                      "Pret":8000,"Carburant":"Benzina","Link":"http://www.google.ro"}
        object = CarObject.carObject(dictionary)

        self.assertItemsEqual(dictionary.values(),[object._Producator,object._Caroserie,
                                                   object._Model,object._AnProductie,object._VolumMotor
                                                    ,object._Pret,object._Carburant,object._Link])

class TestDB(unittest.TestCase):
    def test_DB(self):
        try:
            manager = DatabaseManager.DatabaseManager()
            request= DatabaseManager.DatabaseManager.getSQLqueryFromREST('GE'
                                                                         'T /AutomobileVanzare?Producator=Mercedes&Model=C200&Caroserie=hatchback')
            list = manager.SelectFromDatabase(request)
            print request
            test = 'SELECT * FROM AutomobileVanzare WHERE Producator=\'Mercedes\' AND Model=\'C200\' AND Caroserie=\'hatchback\' '
            self.assertMultiLineEqual(request,test)

            print "Cererea este",request

        except:
            self.assertFalse(True)



class Request(unittest.TestCase):
    def test_request(self):
        request = 'GET /AutomobileVanzare?Pret=1000:5000&Caroserie="Alo"'
        try:
            [theRequest,arguments]=  DatabaseManager.DatabaseManager.split(request,["?"])
        except:
            self.assertFalse(True)
        try:
            [verb,database]=DatabaseManager.DatabaseManager.split(theRequest,["/"])
        except:
            self.assertFalse(True)

if __name__ == '__main__':
    unittest.main()

