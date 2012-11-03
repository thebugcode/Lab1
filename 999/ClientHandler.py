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

import socket
import threading
import pyodbc
import json

class ClientHandler(threading.Thread):
  def __init__(self, client):
    threading.Thread.__init__(self)

    self.__running = False
    self.__socket = client[0]


  def run(self):
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.1.104;DATABASE=Psycar;UID=sa;PWD=Kentsfield1')
    cursor = cnxn.cursor()

    """
    cursor.execute("select Id from Dan")
    row = cursor.fetchall()

    if row:
        print row
    print "Connected"


    cursor.execute("select Id from Dan")
    row = cursor.fetchall()


    if row:
        print row
    print "Connected"
    """

    cursor.execute("SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'Dan1'")
    row = cursor.fetchall()
    print row


"""
for i in range (0,100):
      cursor.execute("insert into Dan(Id) values(" + str(i) + ")")
      cnxn.commit()

for i in range (0,100):
        cursor.execute("delete from Dan where Id = " + str(i) + "")
        print cursor.rowcount, 'products deleted'
        cnxn.commit()

cursor.execute("delete from Dan")
    print cursor.rowcount, 'products deleted'
    cnxn.commit()
"""

"""
    self.__running = True
    while self.__running:
      try:
        # LOGGING
        #data = self.__socket.recv(1024)



        #print self.__socket.getsockname(), "Data received:", data
      except Exception as exc:
        # LOGGING
        print self.__socket.getsockname(), exc
        break
    self
    """