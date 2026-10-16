#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 25 21:14:39 2022

@author: brian
"""
print('\nWelcome to the 2020 Remittance Fee Calculator\n\nUsing this calculator, you will be able to see\njust how much money people from specific countries\naround the world can save from remittance fee\ntransactions if a certain percentage of the country\'s\npopulation switches to the Bitcoin Lightining Network!\n')

import csv



dict_from_csv = {}

with open('data science.csv', mode='r',encoding='utf-8-sig') as FileforPercent:
    reader = csv.reader(FileforPercent)
    dict_for_percent = {rows[0]:rows[1] for rows in reader}


with open('data science.csv', mode='r',encoding='utf-8-sig') as FileforGDP:
    reader2 = csv.reader(FileforGDP)
    dict_for_GDP = {rows[0]:rows[2] for rows in reader2}

for key, value in dict_for_percent.items():
    print(key, value)
    
country_input=input('Above is a list of countries in the world with the percentage\nof their GDP made up from personal remittance fees next to them.\nThese are the top 36 countries in the world with the highest\npercentage of their GDP made up from personal remittance fees.\n\nPlease enter the name of the country you want to explore from this list: ')
country_input=country_input.capitalize()

BTC_adpotance_input=input('Please enter the percent of Bitcoin adoption from 0% to 99%: ')
BTC_adpotance_input=float(BTC_adpotance_input)

def get_percent():
    n = dict_for_percent[country_input]
    n=n.replace('%','')
    n=float(n)
    n=n*0.01
    return n

def get_GDP():
    s = dict_for_GDP[country_input]
    s = s.replace(',','')
    s = float(s)
    return s

total_remittance_fees=get_percent()*get_GDP()*0.11

def percent_of_BTC_adoptance():
    b = BTC_adpotance_input*0.01
    b = b*total_remittance_fees
    return b




BTC_adoptance_input=BTC_adpotance_input*0.01
percent_of_GDP_saved=percent_of_BTC_adoptance()/get_GDP()


print("\nWith a Gross Domestic Product (GDP) of "+"${:,.2f}".format(get_GDP())+" and "+"{:.0%}".format(get_percent())+" of "+country_input+"\'s GDP being made up of remittance fee transactions, "+country_input+' would save '+"${:,.2f}".format(percent_of_BTC_adoptance())+" if "+"{:.0%}".format(BTC_adoptance_input)+" of the population adopted the Bitcoin Lightning Network! This means that the Lightining Network would add a "+"{:.3%}".format(percent_of_GDP_saved)+" increase to "+country_input+'\'s GDP.')

import matplotlib.pyplot as plt
   
PercentageofBitcoinAdoptance = ['5','10','15','20','25','30','35','40','45','50','55','60','65','70','75','80','85','90','95','100']
AmountofMoneySaved = ["${:,.0f}".format(total_remittance_fees*0.05),"${:,.0f}".format(total_remittance_fees*0.1),"${:,.0f}".format(total_remittance_fees*0.15),"${:,.0f}".format(total_remittance_fees*0.2),"${:,.0f}".format(total_remittance_fees*0.25),"${:,.0f}".format(total_remittance_fees*0.3),"${:,.0f}".format(total_remittance_fees*0.35),"${:,.0f}".format(total_remittance_fees*0.4),"${:,.0f}".format(total_remittance_fees*0.45),"${:,.0f}".format(total_remittance_fees*0.5),"${:,.0f}".format(total_remittance_fees*0.55),"${:,.0f}".format(total_remittance_fees*0.6),"${:,.0f}".format(total_remittance_fees*0.65),"${:,.0f}".format(total_remittance_fees*0.7),"${:,.0f}".format(total_remittance_fees*0.75),"${:,.0f}".format(total_remittance_fees*0.8),"${:,.0f}".format(total_remittance_fees*0.85),"${:,.0f}".format(total_remittance_fees*0.9),"${:,.0f}".format(total_remittance_fees*0.95),"${:,.0f}".format(total_remittance_fees)]

plt.bar(PercentageofBitcoinAdoptance, AmountofMoneySaved)
plt.title('Percentage of Bitcoin Adoptance Vs Money Saved')
plt.xlabel('Percentage of Bitcoin Adoptance for '+country_input)
plt.ylabel('Money Saved in US Dollars')
plt.show()