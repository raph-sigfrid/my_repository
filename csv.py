import csv
import sys
import os

input_file = r"C:\Users\mwalu\OneDrive\Desktop\python1\csv.py"
input_file

#returns the csv as a list of lists where each row
data = list(csv.reader(open(input_file),delimiter = ','))

row1 = data[1]
