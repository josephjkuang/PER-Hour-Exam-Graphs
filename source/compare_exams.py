import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import scipy
import pandas as pd
from scipy import stats

# Constants
early_time = -24
exam2_path = "../data/Sp21_Physics_211_HE2_data.csv"
exam3_path = "../data/Sp21_Physics_211_HE3_data.csv"

# Data
exam2_scores = []
exam3_scores = []

difference = []
counting_numbers = []

both_early = []
one_early = []
first_early = []
last_early = []
not_early = []
no_pt = []

delayed_last = []
immediate_last = []

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

def draw_graph(name):
	# Scatter Plot
	plt.scatter(exam2_scores, exam3_scores, alpha=0.5)
	plt.title(name)
	plt.xlabel('Exam 2 Scores')
	plt.ylabel('Exam 3 Scores')

	# Getting R and Slope
	result = scipy.stats.linregress(exam2_scores, exam3_scores)
	r_value = result.rvalue
	slope = result.slope
	print("R-value: " + str(r_value))
	print("R^2 Value: " + str(r_value * r_value))
	print()
	print("Slope: " + str(slope))

	# Combining Earlier Result
	x_line = np.linspace(0, 200, 100) # this creates a list of points for x axis
	plt.xlim([0, 105]) # this defines the range of the axes
	plt.ylim([0, 105])
	plt.plot(x_line, x_line * slope + result.intercept, color='black') # now plot the linear function y = a * x + b
	plt.savefig("../graphs/" + name + ".png")
	plt.show()

def draw_difference(name):
	# Scatter Plot
	plt.scatter(counting_numbers, difference, alpha=0.5)
	plt.title(name)
	plt.xlabel('Students')
	plt.ylabel('Score Difference (Exam 3 - Exam 2)')
	plt.xlim([0, len(difference)]) # this defines the range of the axes
	plt.ylim([-105, 105])
	# plt.savefig("../graphs/" + name + ".png")
	plt.show()

def draw_histogram(name, list, color):
	def_bins = np.linspace(-80, 80, num=33) 
	n, bins, patches = plt.hist(list, bins = def_bins, facecolor = color, ec = 'black')
	plt.title(name)
	plt.xlabel("Score Difference (Exam 3 - Exam 2)")
	plt.ylabel("Number of Students")
	plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
	plt.savefig("../graphs/" + name + ".png")
	plt.show()
	plt.clf()

	print(name)
	print("Mean: " + str(np.mean(list)))
	print("Standard Deviation: " + str(np.std(list)))
	print()

r_list2 = store_file_data(exam2_path)
r_list3 = store_file_data(exam3_path)

parse_file(r_list2, r_list3)
# draw_graph("Exam 2 Versus 3 Scores")
# print("Exam 2 Average: " + str(np.mean(exam2_scores)))
# print("Exam 3 Average: " + str(np.mean(exam3_scores)))

draw_difference("Score Change")

# draw_histogram("Score Difference Histogram Expanded ", difference, "purple")
# draw_histogram("Both Early Score Difference Histogram Expanded", both_early, "green")
# draw_histogram("One Early Score Difference Histogram Expanded", one_early, "blue")
# draw_histogram("One Late Score Difference Histogram Expanded", not_early, "red")
# draw_histogram("No Practice Test Score Difference Histogram Expanded", no_pt, "cyan")
# draw_histogram("Delayed Feedback for Exam 3 Score Difference Histogram Expanded", delayed_last, "yellow")
# draw_histogram("Immediate Feedback for Exam 3 Score Difference Histogram Expanded", immediate_last, "maroon")
# draw_histogram("Early For Exam 2 Score Difference Histogram Expanded", first_early, "teal")
# draw_histogram("Early for Exam 3 Score Difference Histogram Expanded", last_early, "orange")

