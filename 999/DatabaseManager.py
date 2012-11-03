
import pyodbc
import  logging
import re
import CarObject
#run tests
"""
#-------------------------------------------------------------------------------
# Name:        DatabaseManager
# Purpose:
#
# Author:      Dan
#
# Created:     03.11.2012
# Copyright:   ( c ) Dan 2012
# Usage:
    manager = DatabaseManager.DatabaseManager()
    print manager.queryDatabase("Select * From AutomobileVanzare")

#-------------------------------------------------------------------------------
"""
class DatabaseManager:
    def __init__(self,databaseIP='localhost',databaseName='Psycar',userID='sa',userPssword='Kentsfield1'):

        try:
            #The connectionString is used to connect to the database
            connectionString = 'DRIVER={SQL Server};SERVER='+databaseIP+';DATABASE='+databaseName+';UID='+userID+';PWD='+userPssword
            #connect to the database
            self.cnxn = pyodbc.connect(connectionString)
            #get the conexion cursor
            self.cursor = self.cnxn.cursor()
        except:
            logging.error('DatabaseManager - Error Connecting to database')
    #This function is only used for select like querries.
    def SelectFromDatabase(self,query):
        logging.warning("DatabaseManager - Querrying database with "+query)
        try:
            #execute the db query
            self.cursor.execute(query)
            #get the answers into a list
            ListOfCars = self.cursor.fetchall()
        except:
            logging.error('DatabaseManager - Error Executing SQL query '+query)
        #retunrn the list of cars
        #answer is a list of car objects
        answer = []
        for carArray in ListOfCars:
                dictionary= {"Caroserie":carArray[1],"Model":carArray[3],"Producator":carArray[2],
                             "AnProductie":carArray[4],"VolumMotor":carArray[5],
                             "Pret":carArray[6],"Carburant":carArray[7],
                             "Link":carArray[8]}
                answer.append(CarObject.CarObject(dictionary))
        return answer


    def insertDatabase(self,querry):
        #comment
        x=0


     #function for splitting a string into parts given separators
    @staticmethod
    def split(txt, seps):
        default_sep = seps[0]
        for sep in seps[1:]: # we skip seps[0] because that's the default seperator
            txt = txt.replace(sep, default_sep)
        return [i.strip() for i in txt.split(default_sep)]
    #this function return the SQL Querry from a request.


    @staticmethod
    def getSQLqueryFromREST(request):
         SQLQuery = ''

            #As an example suppose request = 'GET /AutomobileVanzare?Pret=0:1000&VolumMotor=0:1800&AnProductie=1990:2010
         [theRequest,arguments]= DatabaseManager.split(request,['?'])
            #Now theRequest = 'GET /AutomobileVanzare' and arguments = 'Pret=0:1000&VolumMotor=0:1800&AnProductie=1990:2010'
         command,table= DatabaseManager.split(theRequest,[" /"])
            #Now command = 'GET' and table= 'AutomobileVanzare'
         if command =='GET':
             SQLQuery += 'SELECT * FROM '
             SQLQuery += table
             SQLQuery+=" WHERE "
             arrayOfParameters = DatabaseManager.split(arguments,["&"])
             k=0
             for params in arrayOfParameters:
                 [parameter,values]=DatabaseManager.split(params,["="])
                 if parameter == "Producator" or parameter == "Model"or parameter == "Caroserie":
                    #If we are not at the last non-numeric paramter then add and AND

                    SQLQuery+=  str(parameter) + "="+chr(39)+str(values)+chr(39)+" AND "
                    k+=1
                 else:
                    [min,max]=DatabaseManager.split(values,[":"])
                    SQLQuery+= parameter
                    SQLQuery +='<'+max
                    SQLQuery+=' AND '+parameter
                    SQLQuery+=">"+min
                    SQLQuery+=" AND "
                    k+=1
             if arrayOfParameters.__len__() ==k:
                SQLQuery =SQLQuery[:-4]

         return SQLQuery





