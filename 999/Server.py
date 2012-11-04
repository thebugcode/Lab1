#-------------------------------------------------------------------------------
# Name:        Server
# Purpose:
#
# Author:      Vlad
#
# Created:     02.11.2012
# Copyright:   (c) Vlad 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pyodbc
from Configurations import server as ServerConfig
from ClientHandler import ClientHandler

import socket
import threading

class Server(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)

    self.__host = ServerConfig.host
    self.__port = ServerConfig.port
    self.__backlog = ServerConfig.backlog
    self.__alive = ServerConfig.alive
    self.__timeout = ServerConfig.timeout
    self.__socket = None


  def run(self):
    while(1):
      self.__socket = socket.socket();
      self.__socket.bind ((self.__host, self.__port))
      self.__socket.listen(self.__backlog)
      self.__socket.settimeout(self.__timeout)

      while(self.__alive):
        # Accept a new client
        client = self.__socket.accept()
        print "New Client:", client[0]

        # Open a new handler
        clientHandler = ClientHandler(client)
        clientHandler.start()

      self.__socket.close()


test = Server()
test.run()
print "Done"













"""
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.1.101;DATABASE=Psycar;UID=sa;PWD=Kentsfield1')
cursor = cnxn.cursor()

cursor.execute("select * from AutomobileVanzare")
row = cursor.fetchall()

if row:
  print row
print "Connected"
"""



"""
  Use a refresh method:
    Other names: refresh, syncWithConfigurations, getConfigurations
    This method refreshes all configurations.

    Usefull in case configurations are changed
    and you want the server to continue running.
"""