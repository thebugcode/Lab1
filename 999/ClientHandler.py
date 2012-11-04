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
      except Exception as exc:
        print self._socket.getsockname(), exc
        break

      # Database connection
      db = DatabaseManager(DatabaseConfig.host)

      # Get SQL Query from REST
      sqlQuery = DatabaseManager.getSQLqueryFromREST(restQuery)

      # Get the result from SQL Server
      carObjects = db.SelectFromDatabase(sqlQuery)

      # Build a JSON String from the result
      jsonString = JSONBuilder.getJSON(carObjects)

      #Send to the server the result
      self._socket.send(jsonString)

    self._socket.close()