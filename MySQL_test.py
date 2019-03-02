# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 12:00:36 2019

@author: XPS15
"""

import mysql.connector

# Obtain connection string information from the portal
mydb = mysql.connector.connect(
  host='localhost',
  user='peijunwang',
  password='123456',
  db='asx'
)

cur= mydb.cursor()

cur.execute("SELECT * FROM anz")



cur.close()  
mydb.close()
