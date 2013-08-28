#!python3.3
# -*- coding: utf-8 -*-
import numpy as np
import os

os.chdir(r"C:\Shares\Server1\data\130815AMO_data") #change directory
os.getcwd() #confirm current directory

filename = "AKB.csv"

amo = np.genfromtxt(filename,
                    delimiter=",",
                    skip_header=5,
                    names = ["V1","V2","V3","V4","V5","V6","V7","V8","V9",
                             "V10","V11","V12","V13","V14","V15","V16","V17",
                             "V18","V19","V20","V21","V22","V23","V24","V25",
                             "V26","V27","V28","V29","V30","V31","V32","V33",
                             "V34","V35","V36"],
                    dtype = [('V1',str),('V2',int),('V3',int),('V4',str),('V5',str),
                           ('V6',str),('V7',int),('V8',int),('V9',int),('V10',int),
                           ('V11',float),('V12',int),('V13',int),('V14',int),
                           ('V15',int),('V16',int),('V17',int),('V18',float),
                           ('V19',float),('V20',float),('V21',float),('V22',float),
                           ('V23',int),('V24',int),('V25',int),('V26',int),('V27',int),
                           ('V28',float),('V29',int),('V30',int),('V31',int),('V32',int),
                           ('V33',int),('V34',int),('V35',int),('V36',int)],
                    filling_values = "-100000"
                    )

print(amo.shape)
print(amo)