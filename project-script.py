import pandas
# need pandas to import dataset
import numpy
# need numpy for numerical analysis
import matplotlib.pyplot as plt
# need this to plot visual representation of data
import csv
# need csv for file reading and writing

def np_from_csv(csv_file):
    temp_data = pandas.read_csv(csv_file, header = None)
    data = temp_data.to_numpy()
    return data
# need this to import a csv file as pandas and change it to numpy array

data = np_from_csv('pima-indians-diabetes.csv')
# stored my csv file as data

def dynamic_plot(data):
    xx= input ("Which column do you want to plot: (ex: 1,2,3, etc.) ")
    x = data[:,int(xx)]
    plt.hist(x, bins = 50)
    yy= input ("What's the x axis label: ")
    plt.xlabel(str(yy))
    zz= input ("What's the y axis label: ")
    plt.ylabel(str(zz))
    aa= input ("What's the graph title: ")
    plt.title (str(aa))
     plt.show()
# created a function that will allow the creation of a histogram depending on chosen variables and data
# this is robust bc it allows the user to create a histogram with chosen data
# also allows user to self name the axes titles and overall figure title

def individual_data([int(x)]):
	x = input ("Which patient do you want to select? (ex: 1,2,3 etc.) ")
	y = data[int(x), :]
	print (list(y))
# this function takes data from a specified row aka a specific patient and outputs their data (from columns) as a list
# with this, the user would then be able to manipulate data within a patient's record
# this is helpful in cases where data might have been inuptted wrong
# or in cases where they are analyzing data and may need to change a null/0 value to something that works

def column_data:
	for column in data:
		a = input ("Which column do you want to select? (ex: 1,2,3,etc.) ")
		max_data = numpy.max(column[a])
		min_data = numpy.min(column[a])
		mean_data = numpy.mean(column[[a])
		median_data = numpy.median(column[a])
		mode_data = numpy.mode(column[a])
	print ("the max of the data is " + str(max_data) \n "the min of the data is " + str(min_data) \n "the mean of the data is " + str(mean_data) \n "the median of the data is " + str(median_data) \n "the mode of the data is " +str(mode_data)
# this function takes into consideration all the data (rom columns) that is being recorded
# allows the user to choose a specific column and outputs the min, max, median, mode and mean of the data

#Assert Conditions

print (max_data)
Assert(max_data) >= 3
# since the previous function allows the user to choose which column they would like to run basic statistical analysis on,
# I kept the assert function general bc the value compared to the data value you expect would change
# this value would then depend on whether you want to run the assert statement on the min, max, median, mode, or mean

# if the max of the specified column was more than or equal to 3, then an error message would not pop up
# this means that the statement is true
# however, if we were to manipulate it so that it compared the min_data with the assert condition:
# print (min_data)
# Assert (min_data) >= 3
# and the min_data is actually the value of 1.243 (or anything less than the value of 3),
# then the AssertError would pop up since this would be a false statement (as in 1.243 is smaller than 3)
