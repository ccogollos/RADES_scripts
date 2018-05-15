################################################################### 
# Script for generating sweeping files for a given RADES geometry #
# Author: Cristian Cogollos                                       #
# Last Edition: 23-04-2018                                        #
###################################################################

import random

params=[]

#Reading the data from the input file
input_file = raw_input('Introduce the input file name (include its extension): ' )
with open(input_file,"r") as infile:
	for i,line in enumerate(infile):
		if i < 5:
			pass
		elif i == 5:
			ports == line[line.find(':')+2:]
		elif i == 6:
			read_data = line[line.find(":")+2:]
			params.append(float(read_data))
		elif i > 6:
			read_data = line[line.find(",")+1:line.find(")")]
			params.append(float(read_data))

output_file = raw_input('Introduce the output file name (do not include the .txt extension): ')
runs = int(raw_input('Introduce the desired number of simulation runs: '))

#Recording the data into the output file
with open(output_file + '.txt',"w") as outfile:
	outfile.write('dl1\t')
	outfile.write('dl' + str(int(params[0])) + '\t')
	for i in range(int(params[0])-2):
		outfile.write('dl' + str(i+2) + '\t')
	for i in range(int(params[0])):
		outfile.write('da' + str(i+1) + '\t')
	for i in range(int(params[0])):
		outfile.write('db' + str(i+1) + '\t')
	for i in range(int(params[0])-1):
		outfile.write('dt' + str(i+1) + '\t')
	for i in range(int(params[0])-1):
		outfile.write('dai' + str(i+1) + '\t')
	for i in range(int(params[0])-1):
		outfile.write('dbi' + str(i+1) + '\t')
	if ports == 'y':
		outfile.write('dlhot1\t')
		outfile.write('dlhot2\t')
		outfile.write('despx1\t')
		outfile.write('despx2\t')
		outfile.write('despz1\t')
		outfile.write('despz2')
	outfile.write('\n')
	for i in range(runs):
		for j,k in enumerate(params):
			if j == 0 :
				pass
			#Generating dlfs
			elif j == 1 :
				for l in range(2):
					num=random.gauss(0,k)
					outfile.write( str(num) + '\t')
			#Generating dlc
			elif j == 2 :
				for l in range(int(params[0])-2):
					num=random.gauss(0,k)
					outfile.write( str(num) + '\t')
			#Generating da
			elif j == 3:
				for l in range(int(params[0])):
					num=random.gauss(0,k)
					outfile.write( str(num) + '\t')
			#Generating db
			elif j == 4:
				for l in range(int(params[0])):
					num=random.gauss(0,k)
					outfile.write( str(num) + '\t')
			#Generating dt
			elif j == 5:
				for l in range(int(params[0])-1):
					num=random.gauss(0,k)
					outfile.write( str(num) + '\t')
			#Generating dai
			elif j == 6:
				for l in range(int(params[0])-1):
					num=random.gauss(0,k)
					outfile.write( str(num) + '\t')
			#Generating dbi
			elif j == 7:
				for l in range(int(params[0])-1):
					num=random.gauss(0,k)
					outfile.write( str(num) + '\t')
			if ports == 'y':
				#Generating dlhot1, dlhot2, despx1, despx2 and despz1
				elif j > 6 and j < 12:
					num=random.gauss(0,k)
					outfile.write( str(num) + '\t')
				#Generating dlhot1, dlhot2, despx1, despx2 and despz2
				elif j == 12:
					num=random.gauss(0,k)
					outfile.write( str(num) + '\n')
			else:
				pass

outfile.close() 

