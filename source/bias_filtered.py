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
		if row[1] != "NULL" and row[1] != "EX" and row[3] != "NULL": # Why are the EX's?
			if row[8] == "NULL":
				if float(row[3]) > 100: # This is for typos with extra zeros
						row[3] = 100
				if float(row[1]) - float(row[3]) > 0:
					no_feedback_bias.append(abs(float(row[1]) - float(row[3])))
			elif float(row[8]) <= early_time:
				if float(row[3]) > 100: # This is for typos with extra zeros
						row[3] = 100

				if float(row[1]) - float(row[3]) > 0:
					if int(row[5]) == 1:
						delayed_feedback_early_bias.append(abs(float(row[1]) - float(row[3])))
					else:
						immediate_feeback_early_bias.append(abs(float(row[1]) - float(row[3])))
			elif float(row[8]) < 0: # Sometimes students finish practice after exam time?
				if float(row[3]) > 100: # This is for typos with extra zeros
						row[3] = 100

				if float(row[1]) - float(row[3]) > 0:
					if int(row[5]) == 1:
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

	# print(delayed_means)
	# print()
	# print(immediate_means)
	# print()
	# print(no_means)

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

def remove_outliers():
	outside = np.mean(delayed_feedback_early_bias) + 2 * np.std(delayed_feedback_early_bias)
	for i in range(len(delayed_feedback_early_bias)):
		if delayed_feedback_early_bias[len(delayed_feedback_early_bias) - i - 1] > outside:
			delayed_feedback_early_bias.remove(delayed_feedback_early_bias[len(delayed_feedback_early_bias) - i - 1])

	outside = np.mean(delayed_feedback_late_bias) + 2 * np.std(delayed_feedback_late_bias)
	for i in range(len(delayed_feedback_late_bias)):
		if delayed_feedback_late_bias[len(delayed_feedback_late_bias) - i - 1] > outside:
			delayed_feedback_late_bias.remove(delayed_feedback_late_bias[len(delayed_feedback_late_bias) - i - 1])

	outside = np.mean(immediate_feeback_early_bias) + 2 * np.std(immediate_feeback_early_bias)
	for i in range(len(immediate_feeback_early_bias)):
		if immediate_feeback_early_bias[len(immediate_feeback_early_bias) - i - 1] > outside:
			immediate_feeback_early_bias.remove(immediate_feeback_early_bias[len(immediate_feeback_early_bias) - i - 1])

	outside = np.mean(immediate_feeback_late_bias) + 2 * np.std(immediate_feeback_late_bias)
	for i in range(len(immediate_feeback_late_bias)):
		if immediate_feeback_late_bias[len(immediate_feeback_late_bias) - i - 1] > outside:
			immediate_feeback_late_bias.remove(immediate_feeback_late_bias[len(immediate_feeback_late_bias) - i - 1])

	outside = np.mean(no_feedback_bias) + 2 * np.std(no_feedback_bias)
	for i in range(len(no_feedback_bias)):
		if no_feedback_bias[len(no_feedback_bias) - i - 1] > outside:
			no_feedback_bias.remove(no_feedback_bias[len(no_feedback_bias) - i - 1])

r_list = store_file_data(exam2_path)
parse_file()
remove_outliers()
draw_graph("Filtered Hour Exam 2 Metacognitive Bias of Underestimators")
clear_lists()

r_list = store_file_data(exam3_path)
parse_file()
remove_outliers()
draw_graph("Filtered Hour Exam 3 Metacognitive Bias of Underestimators")

# print()
# print(len(delayed_feedback_early_bias))
# print(len(immediate_feeback_early_bias))
# print(len(delayed_feedback_late_bias))
# print(len(immediate_feeback_late_bias))
# print(len(no_feedback_bias))
