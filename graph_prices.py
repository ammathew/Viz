import requests
import csv
from numpy import genfromtxt
import numpy as np

url = 'http://finance.google.co.uk/finance/historical?q=LON:VOD&startdate=Oct+1,2008&enddate=Oct+9,2008&output=csv'
res = requests.get(url)
prices_csv = res.text.encode('utf-8')

print prices_csv

file = open("temp.csv", "w")
file.write( prices_csv )

my_data = genfromtxt('temp.csv', delimiter=",", names=True, skip_footer=1)

print my_data
print my_data['Close']
