# Small program to minimize weighted sum of completion times

# Prereqs:
# File "jobs.txt" with the format
#
# [number_of_jobs]
# [job_1_weight] [job_1_length]
# [job_2_weight] [job_2_length]

# All jobs have positive, integer costs.
# This is a greedy algorithm

# The returns the sum of the minimized completion times based on
# two different greedy criteria

import operator # For itemgetter
f = open('jobs.txt','r')
a = [line.strip().split() for line in f] # Split each line
f.close()
a = [[int(column) for column in row] for row in a]
num = a.pop(0) # remove the top row to get the number of jobs
for i in xrange(num[0]): 
# Add two new columns to the array, one with difference, one with ratio
	a[i].append(a[i][0] - a[i][1])
	a[i].append(float(a[i][0])/a[i][1])
	
# For when ratio is greedy criteria
a.sort(key = operator.itemgetter(3, 0), reverse = True)
# For when difference is greedy criteria
# a.sort(key = operator.itemgetter(2, 0), reverse = True)
total = 0
completion = 0
for i in a:
	completion += i[1] # Add to the completion time
	total += completion*i[0] # Add the cost
print total