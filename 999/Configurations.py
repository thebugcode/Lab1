#-------------------------------------------------------------------------------
# Name:        configurations
# Purpose:     stores configurations
#
# Author:      Vlad
#
# Created:     02.11.2012
# Copyright:   (c) Vlad 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
""" One does not simply make changes in this class """

class server:
  host = "192.168.1.103"
  port = 2707
  backlog = 5 # waiting queue length
  timeout = None

  """
  CAUTION
  This variable represents the state of the server:
    0 - server down
    1 - server up
  """
  alive = 1