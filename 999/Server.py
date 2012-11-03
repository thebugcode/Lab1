#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Vlad
#
# Created:     02.11.2012
# Copyright:   (c) Vlad 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import Configurations
from ClientHandler import ClientHandler

import socket
import threading

class Server(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)

    self.__host = Configurations.server.host
    self.__port = Configurations.server.port
    self.__backlog = Configurations.server.backlog
    self.__alive = Configurations.server.alive
    self.__timeout = Configurations.server.timeout
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
        print "New Client"
        clientHandler = ClientHandler(client)
        clientHandler.start()
        print "New Client"

      self.__socket.close()



test = Server()
test.run()
print "Done"















"""
  Use a refresh method:
    Other names: refresh, syncWithConfigurations, getConfigurations
    This method refreshes all configurations.

    Usefull in case configurations are changed
    and you want the server to continue running.
"""