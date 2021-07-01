import csv  # to read csv files
import numpy as np  # to use statistics functions
import matplotlib.pyplot as plt
import scipy
import pandas as pd
from scipy import stats


# Data
delayed_feedback_time = []
delayed_feedback_time = []
immediate_feeback_time = []
immediate_feedback_time = []

# Constants
exam2_path = "../data/Sp21_Physics_211_HE2_data.csv"
exam3_path = "../data/Sp21_Physics_211_HE3_data.csv"

def store_file_data(path): # Opens the CSV Data and Stores the Returns the Data as a List
	with open(path) as file:
		reader = csv.reader(file)
		r_list = [r for r in reader]  # convert csv file to a python list
		labels = r_list.pop(0)
	return r_list

def store_file_data(path): # Opens the CSV Data and Stores the Returns the Data as a List
	with open(path) as file:
		reader = csv.reader(file)
		r_list = [r for r in reader]  # convert csv file to a python list
		labels = r_list.pop(0)
	return r_list

def parse_file(list2, list3): # Dividing the Data into appropriate bins
	count = 0
	for i in range(len(list2) - 1):
		row = list3[0]
		for j in range(len(list3) - 1):
			if list2[i][0] == list3[j][0]:
				row = list3[j]
				list3.pop(j)
				break

		if list2[i][1] != "NULL" and row[1] != "NULL" and list2[i][0] == row[0]:
			exam2_scores.append(float(list2[i][1]))
			exam3_scores.append(float(row[1]))

			difference.append(float(row[1]) - float(list2[i][1]))
			counting_numbers.append(i)

			if list2[i][8] != "NULL" and float(list2[i][8]) <= early_time:
				if row[8] != "NULL" and float(row[8]) <= early_time:
					both_early.append(float(row[1]) - float(list2[i][1]))
				else:
					first_early.append(float(row[1]) - float(list2[i][1]))
					one_early.append(float(row[1]) - float(list2[i][1]))
			elif row[8] != "NULL" and float(row[8]) <= early_time:
				last_early.append(float(row[1]) - float(list2[i][1]))
				one_early.append(float(row[1]) - float(list2[i][1]))
			elif float(list2[i][6]) == 0 and float(row[6]):
				no_pt.append(float(row[1]) - float(list2[i][1]))
			else:
				not_early.append(float(row[1]) - float(list2[i][1]))

			if row[5] != "NULL":
				if row[5] != "1":
					delayed_last.append(float(row[1]) - float(list2[i][1]))
				else:
					immediate_last.append(float(row[1]) - float(list2[i][1]))
		else:
			count += 1
	print(str(count) + " ids were not found between both exams\n")
	