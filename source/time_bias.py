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

def parse_file(): # Dividing the Data into appropriate bins
	for row in r_list:
		if row[1] != "NULL" and row[1] != "EX" and row[8] != "NULL" and float(row[8]) <= 0:
			if int(row[5]) == 1:
				delayed_feedback_time.append(float(row[1]))
				delayed_feedback_time.append(abs(float(row[8])))
			else:
				immediate_feeback_time.append(float(row[1]))
				immediate_feedback_time.append(abs(float(row[8])))

def draw_graph(name):
	# Scatter Plot
	plt.scatter(immediate_feedback_time, immediate_feeback_time, alpha=0.5)
	plt.title(name)
	plt.xlabel('Hours Before Exam')
	plt.ylabel('Time')

	# Getting R and Slope
	result = scipy.stats.linregress(immediate_feedback_time, immediate_feeback_time)
	r_value = result.rvalue
	slope = result.slope
	print("R-value: " + str(r_value))
	print("R^2 Value: " + str(r_value * r_value))
	print()
	print("Slope: " + str(slope))

	# Combining Earlier Result
	x_line = np.linspace(0, 200, 100) # this creates a list of points for x axis
	plt.xlim([0, 200]) # this defines the range of the axes
	plt.ylim([0, 105])
	plt.plot(x_line, x_line * slope + result.intercept, color='black') # now plot the linear function y = a * x + b
	plt.savefig("../graphs/" + name + ".png")
	plt.show()

r_list = store_file_data(exam2_path)
parse_file()
# r_list = store_file_data(exam3_path)
# parse_file()
draw_graph("Delayed Feedback Score by Time")
