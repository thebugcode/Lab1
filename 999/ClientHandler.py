#-------------------------------------------------------------------------------
# Name:        ClientHandler
# Purpose:     Handles a CLient
#
# Author:      Vlad
#
# Created:     03.11.2012
# Copyright:   (c) Vlad 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import socket
import threading
from Configurations import database as DatabaseConfig
from DatabaseManager import DatabaseManager
from JSONBuilder import JSONBuilder

class ClientHandler(threading.Thread):
  def __init__(self, client):
    threading.Thread.__init__(self)
    self._running = False
    self._socket = client[0]


  def run(self):
    self._running = True
    while self._running:
      try:
        restQuery = self._socket.recv(1024)
        print restQuery
        #restQuery = restQuery[10:]
      except Exception as exc:
        # LOGGING
        print self._socket.getsockname(), exc
        break
      db = DatabaseManager(DatabaseConfig.host)

      sqlQuery = DatabaseManager.getSQLqueryFromREST(restQuery)
      carObjects = db.SelectFromDatabase(sqlQuery)

      print carObjects
      jsonString = JSONBuilder.getJSON(carObjects)
      print jsonString
      self._socket.send(jsonString)

    self