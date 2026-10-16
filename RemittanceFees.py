#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 23 14:14:51 2022

@author: brian
"""

import csv

file=open('data science.csv')
csvreader =csv.reader(file)

percent=[]
grossdomesticproduct=[]

for row in csvreader:
    percent.append(row[1])
    grossdomesticproduct.append(row[2])
    
    
print(percent)
print(grossdomesticproduct)

def albania():
    
    
    
