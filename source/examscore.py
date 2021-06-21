import csv  # to read csv files
import numpy as np  # to use statistics functions
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import scipy
import pandas as pd
from scipy import stats

# Data
delayed_feedback_early_score = []
delayed_feedback_late_score = []
no_feedback_score = []
immediate_feeback_early_score = []
immediate_feeback_late_score = []

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
		if row[1] != "NULL" and row[1] != "EX": # Why are the EX's?
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

def draw_graph(name): # Drawing Hour Exam 2 Score by Feedback
	# Calculating the Means
	delayed_means = [np.mean(delayed_feedback_early_score), np.mean(delayed_feedback_late_score)]
	immediate_means = [np.mean(immediate_feeback_early_score), np.mean(immediate_feeback_late_score)]
	no_means = [np.mean(no_feedback_score)]

	# print(delayed_means)
	# print()
	# print(immediate_means)
	# print()
	# print(no_means)

	# Calculating the Error Bars
	delayed_errors = [stats.sem(delayed_feedback_early_score), stats.sem(delayed_feedback_late_score)]
	immediate_errors = [stats.sem(immediate_feeback_early_score), stats.sem(immediate_feeback_late_score)]
	no_errors = [stats.sem(no_feedback_score)]

	# Drawing the Bars
	plt.style.use('classic')
	plt.bar([1, 1.25], delayed_means, width=0.075, color='green', yerr=delayed_errors)
	plt.bar([1.1, 1.35], immediate_means, width=0.075, color='orange', yerr=immediate_errors)
	plt.bar([1.5], no_means, width=0.075, color='gray', yerr=no_errors)
	plt.bar([1.6], 0, width=0.075, color='gray') # Needed to Expand the Graph

	# Labeling the Graph
	plt.ylabel("Exam Score")
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
	delayed_feedback_early_score.clear()
	delayed_feedback_late_score.clear()
	no_feedback_score.clear()
	immediate_feeback_early_score.clear()
	immediate_feeback_late_score.clear()

r_list = store_file_data(exam2_path)
parse_file()
draw_graph("Hour Exam 2 Score by Feedback")
clear_lists()

r_list = store_file_data(exam3_path)
parse_file()
draw_graph("Hour Exam 3 Score by Feedback")

# r_list = store_file_data(exam2_path)
# parse_file()
# r_list = store_file_data(exam3_path)
# parse_file()
# draw_graph("Combined Hour Exam 2 and 3 Score by Feedback")

# print()
# print(len(delayed_feedback_early_score))
# print(len(immediate_feeback_early_score))
# print(len(delayed_feedback_late_score))
# print(len(immediate_feeback_late_score))
# print(len(no_feedback_score))
