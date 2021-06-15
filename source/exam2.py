import csv  # to read csv files
import numpy as np  # to use statistics functions
import matplotlib.pyplot as plt
import scipy
import pandas as pd
from scipy import stats

delayed_feedback_early_score = []
delayed_feedback_late_score = []
no_feedback_score = []
immediate_feeback_early_score = []
immediate_feeback_late_score = []


early_time = -24
exam2_path = "../data/Sp21_Physics_211_HE2_data.csv"

def store_file_data(path): # Opens the CSV Data and Stores the Returns the Data as a List
	with open(path) as file:
		reader = csv.reader(file)
		r_list = [r for r in reader]  # convert csv file to a python list
		labels = r_list.pop(0)
	return r_list

def parse_file():
	for row in r_list:
		if row[1] != "NULL" and row[1] != "EX":
			if row[8] == "NULL":
				no_feedback_score.append(float(row[1]))
			elif float(row[8]) <= early_time:
				if int(row[5]) == 1:
					delayed_feedback_early_score.append(float(row[1]))
				else:
					immediate_feeback_early_score.append(float(row[1]))
			elif float(row[8]) < 0: # Sometimes students finish practice after exam time?
				if int(row[5]) == 1:
					delayed_feedback_late_score.append(float(row[1]))
				else:
					immediate_feeback_late_score.append(float(row[1]))


r_list = store_file_data(exam2_path)
parse_file()
print(len(no_feedback_score))
print(len(delayed_feedback_early_score))
print(len(immediate_feeback_early_score))
print(len(delayed_feedback_late_score))
print(len(immediate_feeback_late_score))