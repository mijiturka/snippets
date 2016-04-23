# Creates 0-1 entries out of aggregated numbers. For use with binomial functions in R

# Expects columns to be of the form
# 	year, name, token, count0, count1, totalcount, ratio
# (as the ones generated by other scripts in this repository).
# Discards the last two.
# Prints a line with a 0 a *count0* number of times, 1 a *count1* of times.

import glob, os

input_folder = "zeroones-input"
output_folder = "zeroones-output"
io_file_extension=".csv"

input_files = os.path.join(input_folder, '*'+io_file_extension)
read_files = glob.glob(input_files)
read_files.sort()
for file in read_files:
	# create result file
	with open(file, "rb") as infile: 
		result_file = os.path.basename(file).split(io_file_extension)[0] + "_res.csv"
		result_file = os.path.join(output_folder, result_file)
		with open(result_file, "wb") as outfile:
			# Remove trailing column labels we don't need
			firstline = infile.readline().split(", count0")[0]+", value"
			outfile.write(firstline)

			inf = infile.readlines()
			for line in inf:
				line = line.strip()
				year, name, token, count0, count1, totalcount, hoeratio = line.split(",")
				for i in range(0,int(count0)):
					outfile.write(year+", "+name+", "+token+", "+"0\n")
				for i in range(0,int(count1)):
					outfile.write(year+", "+name+", "+token+", "+"1\n")
