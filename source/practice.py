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
exam_score = []
practice_score_first = []
practice_score_last = []
predictions = []

delayed_first_practice = []
delayed_last_practice = []
immediate_first_practice = []
immediate_last_practice = []

delayed_exam = []
immediate_exam = []

def store_file_data(path): # Opens the CSV Data and Stores the Returns the Data as a List
	with open(path) as file:
		reader = csv.reader(file)
		r_list = [r for r in reader]  # convert csv file to a python list
		labels = r_list.pop(0)
	return r_list

def parse_file(r_list): # Dividing the Data into appropriate bins
	for row in r_list:
		if row[9] != "NULL" and row[10] != "NULL" and float(row[9]) != 0 and float(row[10]) != 0:
			exam_score.append(float(row[1]))
			practice_score_first.append(float(row[9]))
			practice_score_last.append(float(row[10]))

			if row[5] == "1":
				delayed_first_practice.append(float(row[9]))
				delayed_last_practice.append(float(row[10]))
				delayed_exam.append(float(row[1]))
			elif row[5] == "0":
				immediate_first_practice.append(float(row[9]))
				immediate_last_practice.append(float(row[10]))
				immediate_exam.append(float(row[1]))

def draw_scatter(name, practices, exams):
	# Scatter Plot
	plt.scatter(practices, exams, alpha=0.5)
	plt.title(name)
	plt.xlabel('Practice Score')
	plt.ylabel('Exam Score')

	# Getting R and Slope
	result = scipy.stats.linregress(practices, exams)
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
	# plt.show()

# r_list = store_file_data(exam2_path)
# parse_file(r_list)
# draw_scatter("First Practice Score Versus Exam 2 Score Scatter Plot", practice_score_first, exam_score)
# draw_scatter("Last Practice Score Versus Exam 2 Score Scatter Plot", practice_score_last, exam_score)
# draw_scatter("Delayed Feedback First Practice Score Verus Exam 2 Score Scatter Plot", delayed_first_practice, delayed_exam)
# draw_scatter("Delayed Feedback Last Practice Score Verus Exam 2 Score Scatter Plot", delayed_last_practice, delayed_exam)
# draw_scatter("Immediate Feedback First Practice Score Verus Exam 2 Score Scatter Plot", immediate_first_practice, immediate_exam)
# draw_scatter("Immediate Feedback Last Practice Score Verus Exam 2 Score Scatter Plot", immediate_last_practice, immediate_exam)

r_list = store_file_data(exam3_path)
parse_file(r_list)
# draw_scatter("First Practice Score Versus Exam 3 Score Scatter Plot", practice_score_first, exam_score)
# draw_scatter("Last Practice Score Versus Exam 3 Score Scatter Plot", practice_score_last, exam_score)
# draw_scatter("Delayed Feedback First Practice Score Verus Exam 3 Score Scatter Plot", delayed_first_practice, delayed_exam)
# draw_scatter("Delayed Feedback Last Practice Score Verus Exam 3 Score Scatter Plot", delayed_last_practice, delayed_exam)
# draw_scatter("Immediate Feedback First Practice Score Verus Exam 3 Score Scatter Plot", immediate_first_practice, immediate_exam)
# draw_scatter("Immediate Feedback Last Practice Score Verus Exam 3 Score Scatter Plot", immediate_last_practice, immediate_exam)

