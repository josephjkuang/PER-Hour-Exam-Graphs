import csv  # to read csv files
import numpy as np  # to use statistics functions
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import scipy
import pandas as pd
from scipy import stats

# Data
delayed_feedback_early_bias = []
delayed_feedback_late_bias = []
no_feedback_bias = []
immediate_feeback_early_bias = []
immediate_feeback_late_bias = []

# Constants
early_time = -24
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
		if row[3] != "NULL": # Removing people without predictions
			if float(row[1]) - float(row[3]) > 0: # Filters for Underestimators
				if row[5] == "NULL" or float(row[6]) == 0: # People who did not have any practice questions done
					no_feedback_bias.append(abs(float(row[1]) - float(row[3])))
				elif row[8] == "NULL" and float(row[6]) > 0: # People who did less than 20 questions late
					if row[5] == "1":
						delayed_feedback_late_bias.append(abs(float(row[1]) - float(row[3])))
					else:
						immediate_feeback_late_bias.append(abs(float(row[1]) - float(row[3])))
				elif float(row[8]) <= early_time: # People who did 20 practice questions early
					if row[5] == "1":
						delayed_feedback_early_bias.append(abs(float(row[1]) - float(row[3])))
					else:
						immediate_feeback_early_bias.append(abs(float(row[1]) - float(row[3])))
				elif float(row[8]) <= 0: # People who did 20 practice questions late
					if row[5] == "1":
						delayed_feedback_late_bias.append(abs(float(row[1]) - float(row[3])))
					else:
						immediate_feeback_late_bias.append(abs(float(row[1]) - float(row[3])))

def draw_graph(name): # Drawing Hour Exam 2 Score by Feedback
	# Calculating the Means
	delayed_means = [np.mean(delayed_feedback_early_bias), np.mean(delayed_feedback_late_bias)]
	immediate_means = [np.mean(immediate_feeback_early_bias), np.mean(immediate_feeback_late_bias)]
	no_means = [np.mean(no_feedback_bias)]

	# Calculating the Error Bars
	delayed_errors = [stats.sem(delayed_feedback_early_bias), stats.sem(delayed_feedback_late_bias)]
	immediate_errors = [stats.sem(immediate_feeback_early_bias), stats.sem(immediate_feeback_late_bias)]
	no_errors = [stats.sem(no_feedback_bias)]

	print(delayed_means)
	print()
	print(immediate_means)
	print()
	print(no_means)

	# Drawing the Bars
	plt.style.use('classic')
	plt.bar([1, 1.25], delayed_means, width=0.075, color='green', yerr=delayed_errors)
	plt.bar([1.1, 1.35], immediate_means, width=0.075, color='orange', yerr=immediate_errors)
	plt.bar([1.5], no_means, width=0.075, color='gray', yerr=no_errors)
	plt.bar([1.6], 0, width=0.075, color='gray') # Needed to Expand the Graph

	# Labeling the Graph
	plt.ylabel("Exam bias")
	labels = ["PT Early", "PT Late", "No PT"]
	plt.xticks([1.05, 1.3, 1.5], labels)
	plt.title(name)

	# Creating the Color Ledgend
	green_patch = mpatches.Patch(color='green', label='Delayed')
	orange_patch = mpatches.Patch(color='orange', label='Immediate')
	gray_patch = mpatches.Patch(color='gray', label='None')
	plt.legend(bbox_to_anchor=(0.82, 0.3), loc='upper left', borderaxespad=0, handles=[green_patch, orange_patch, gray_patch], prop={"size":8})

	plt.savefig("../graphs/" + name + ".png")
	plt.show()

def clear_lists():
	delayed_feedback_early_bias.clear()
	delayed_feedback_late_bias.clear()
	immediate_feeback_early_bias.clear()
	immediate_feeback_late_bias.clear()
	no_feedback_bias.clear()

# r_list = store_file_data(exam2_path)
# parse_file()
# draw_graph("Hour Exam 2 Metacognitive Bias for Underestimators")
# clear_lists()

# r_list = store_file_data(exam3_path)
# parse_file()
# draw_graph("Hour Exam 3 Metacognitive Bias for Underestimators")

r_list = store_file_data(exam2_path)
parse_file()
r_list = store_file_data(exam3_path)
parse_file()
draw_graph("Combined Metacognitive Bias for Underestimators")

print()
print(len(delayed_feedback_early_bias))
print(len(immediate_feeback_early_bias))
print(len(delayed_feedback_late_bias))
print(len(immediate_feeback_late_bias))
print(len(no_feedback_bias))
