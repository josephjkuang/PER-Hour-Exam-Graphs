import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import scipy
from scipy import stats

# Data
exam2_scores = []
exam1_scores = []
delayed_early = []
delayed_late = []
immediate_early = []
immediate_late = []
no_pt = []

# Constants
exam1_path = "../data/Exam1_scores.csv"
exam2_path = "../data/Sp21_Physics_211_HE2_data.csv"
minimum_questions = 10

def store_file_data(path): # Opens the CSV Data and Stores the Returns the Data as a List
	with open(path) as file:
		reader = csv.reader(file)
		r_list = [r for r in reader]  # convert csv file to a python list
		labels = r_list.pop(0)
	return r_list

def parse_file(list2, list1): # Dividing the Data into appropriate bins
	count = 0
	for i in range(len(list2) - 1):
		row = list1[0]
		for j in range(len(list1) - 1):
			if list2[i][0] == list1[j][1]:
				row = list1[j]
				list1.pop(j)
				break

		if list2[i][1] != "NULL" and row[2] != "NULL" and row[2] != "EX" and float(row[2]) != 0 and list2[i][0] == row[1]:
			exam2_scores.append(float(list2[i][1]))
			exam1_scores.append(float(row[2]))

			if list2[i][5] == "NULL" or float(list2[i][6]) < minimum_questions: # People who did not have any practice questions done
				no_pt.append(float(row[2]))
			elif float(list2[i][7]) >= minimum_questions: # People who did the minimum number of questions before for the survey
				if list2[i][5] == "1":
					delayed_early.append(float(row[2]))
				else:
					immediate_early.append(float(row[2]))
			else:
				if float(list2[i][6]) >= minimum_questions: # People who did the minimum number of questions after the survey 
					if list2[i][5] == "1":
						delayed_late.append(float(row[2]))
					else:
						immediate_late.append(float(row[2]))
				else:
					print("This should be unreachable")
		else:
			count += 1
	print(str(count) + " ids were not found between both exams\n")

def draw_graph(name):
	# Calculating the Means
	delayed_means = [np.mean(delayed_early), np.mean(delayed_late)]
	immediate_means = [np.mean(immediate_early), np.mean(immediate_late)]
	no_means = [np.mean(no_pt)]

	# Calculating the Error Bars
	delayed_errors = [stats.sem(delayed_early), stats.sem(delayed_late)]
	immediate_errors = [stats.sem(immediate_early), stats.sem(immediate_late)]
	no_errors = [stats.sem(no_pt)]

	# Printing Relevant Info
	print("Delayed Feedback Early Average " + str(delayed_means[0]) + " for " + str(len(delayed_early)) + " tests")
	print("Immediate Feedback Early Average " + str(immediate_means[0]) + " for " + str(len(immediate_early)) + " tests")
	print("Delayed Feedback Late Average " + str(delayed_means[1]) + " for " + str(len(delayed_late)) + " tests")
	print("Immediate Late Average " + str(immediate_means[0]) + " for " + str(len(immediate_late)) + " tests")
	print("No Practice Test Average " + str(no_means[0]) + " for " + str(len(no_pt)) + " tests")

	# Drawing the Bars
	plt.style.use('classic')
	plt.bar([1, 1.25], delayed_means, width=0.075, color='green', yerr=delayed_errors)
	plt.bar([1.1, 1.35], immediate_means, width=0.075, color='blue', yerr=immediate_errors)
	plt.bar([1.5], no_means, width=0.075, color='black', yerr=no_errors)
	plt.bar([1.6], 0, width=0.075, color='gray') # Needed to Expand the Graph

	# Labeling the Graph
	plt.ylabel("Exam Score")
	labels = ["PT Early", "PT Late", "No PT"]
	plt.xticks([1.05, 1.3, 1.5], labels)
	plt.title(name)
	plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

	# Creating the Color Ledgend
	green_patch = mpatches.Patch(color='green', label='Delayed')
	orange_patch = mpatches.Patch(color='blue', label='Immediate')
	gray_patch = mpatches.Patch(color='gray', label='None')
	plt.legend(bbox_to_anchor=(0.82, 0.3), loc='upper left', borderaxespad=0, handles=[green_patch, orange_patch, gray_patch], prop={"size":8})

	plt.savefig("../graphs2/" + name + ".png")
	plt.show()
	
list1 = store_file_data(exam1_path)
list2 = store_file_data(exam2_path)
parse_file(list2, list1)
draw_graph("Exam 1 Scores")

