import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import scipy
import pandas as pd
from scipy import stats

# Constants
exam2_path = "../data/Sp21_Physics_211_HE2_data.csv"
exam3_path = "../data/Sp21_Physics_211_HE3_data.csv"

# Data
prediction = []
practice_first = []
practice_last = []


def store_file_data(path): # Opens the CSV Data and Stores the Returns the Data as a List
	with open(path) as file:
		reader = csv.reader(file)
		r_list = [r for r in reader]  # convert csv file to a python list
		labels = r_list.pop(0)
	return r_list

def parse_file(r_list): # Dividing the Data into appropriate bins
	for row in r_list:
		if row[9] != "NULL" and row[10] != "NULL" and float(row[9]) != 0 and float(row[10]) != 0 and row[3] != "NULL":
			prediction.append(float(row[3]))
			practice_first.append(float(row[9]))
			practice_last.append(float(row[10]))

def draw_scatter(name, practices, prediction):
	# Scatter Plot
	plt.scatter(practices, prediction, alpha=0.5)
	plt.title(name)
	plt.xlabel('Practice Score')
	plt.ylabel('Prediction Score')

	# Getting R and Slope
	result = scipy.stats.linregress(practices, prediction)
	r_value = result.rvalue
	slope = result.slope
	print("R-value: " + str(r_value))
	print("R^2 Value: " + str(r_value * r_value))
	print("Slope: " + str(slope))

	# Combining Earlier Result
	x_line = np.linspace(0, 200, 100) # this creates a list of points for x axis
	plt.xlim([0, 105]) # this defines the range of the axes
	plt.ylim([0, 105])
	plt.plot(x_line, x_line * slope + result.intercept, color='black') # now plot the linear function y = a * x + b
	plt.savefig("../graphs/" + name + ".png")
	plt.show()

r_list = store_file_data(exam2_path)
parse_file(r_list)
# draw_scatter("Practice First Score Versus Prediction for Exam 2", practice_first, prediction)
# draw_scatter("Practice Last Score Versus Prediction for Exam 2", practice_last, prediction)

# r_list = store_file_data(exam3_path)
# parse_file(r_list)
# draw_scatter("Practice First Score Versus Prediction for Exam 3", practice_first, prediction)
# draw_scatter("Practice Last Score Versus Prediction for Exam 3", practice_last, prediction)
