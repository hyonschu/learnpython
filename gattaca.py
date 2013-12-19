"""
Given a file in the following format:

GATAGGAGTAGTGAGT
GTAGTAGAGTATGATAGTGTA
GATTAGATGATGATG
GATATATAGATATATTAGAT
GATAGATAGT
GATTAAGATATGATAGTAG
GATTAGATAGTAGTAGT
GTATAGATAGTAGTAGTGATGA
GTAGATGATGATAGTAGTAGT
GAAGTAGTGATGAGTAG

For every position in the string, find the breakdown (in percentage) for each symbol encountered. The goal of this exercise is to calculate the population percentages for each symbol in each position, i.e.: what percentage of times do I see symbol X in position Y? From the example input data, we would arrive at the following percentages:
 
Position: 1 (A: 0%,  C: 0%, G: 100%, T: 0%)
"""

def gattaca(filename):
	d=[]
	f=open(filename)
	for line in f:
		line.replace("\n", "") # delete all newline characters
		d.append(list(line)) # turn each line into an array
	data = map(None,*d) # transpose each row into a column, imputate None where there are no entries
	linecount = 1 #
	for j in data: 
		sum = len(j)*1.0
		check = [] # initiate new list for comparison
		for k in j:	
			if k not in check: 
				check.append(k) 
			check.sort() 
		print "\n*** Position %s ***" %linecount
		for l in check:	
			print l,":",(j.count(l)/sum)*100,"%" # return percentages
		linecount += 1
