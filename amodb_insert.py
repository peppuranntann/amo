#!python3.3
# -*- coding: utf-8 -*-
import numpy as np
import sqlite3 as sql3
import os

os.chdir(r"C:/Shares/Server1/data/amo_db") #change directory
os.getcwd() #confirm current directory


filename = ""
dbname = "amo.sqlite3" #######set DB name#########


amo = np.genfromtxt(filename,
                    delimiter="\t",
                    skip_header=5,
                    missing_values = "N/A" )

con = sql3.connect(dbname) # connect the DB
cur = con.cursor() # create cursor

