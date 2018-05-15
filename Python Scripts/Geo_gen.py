############################################## 
# Script for generating RADES geometry files #
# Author: Cristian Cogollos                  #
# Last Edition: 23-04-2018                   #
##############################################

output_file = raw_input('Introduce the output file name (with the desired extension): ')

while True:
	iris_type = raw_input('Are the irises inductive, capacitive or alternated?(i/c/a) ')
	if iris_type == 'i' or iris_type == 'c' or iris_type == 'a':
		break
	else:
		print('Wrong input')

while True:
	ports = raw_input('Does the structure have coaxial ports?(y/n) ')
	if ports == 'y' or ports == 'n':
		break
	else:
		print('Wrong input')

with open(output_file,"w") as outfile:

	for i in range(48):
		outfile.write('#')
	outfile.write('\n')
	outfile.write('#             RADES geometry file              #\n')
	outfile.write('# Notation for each parameter -> (mean, sigma) #\n')
	for i in range(48):
		outfile.write('#')
	outfile.write('\n')

	outfile.write('Irises(i/c/a): ' + iris_type + '\n')
	outfile.write('Ports(y/n): ' + ports + '\n')
	outfile.write('Number of cavities: ' + raw_input('Introduce the number of cavities that constitute the structure: ') + '\n')
	print('Introduce the different dimensions in the following form: (mean value, standard deviation)')
	outfile.write('First/Last cavity l: ' + raw_input('First and last cavity l dimension: ') + '\n')
	outfile.write('Middle cavities l: ' + raw_input('Intermidiate cavities l dimension: ') + '\n')
	a_dim = raw_input('Cavities a dimension (common to capacitive iris): ')
	b_dim = raw_input('Cavities b dimension (common to inductive iris): ')
	outfile.write('Cavities a: ' + a_dim + '\n')
	outfile.write('Cavities b: ' + b_dim + '\n')

	if iris_type == 'i':
		outfile.write('Iris l: ' + raw_input('Iris l dimension: ') + '\n')
		outfile.write('Iris a: ' + raw_input('Iris a dimension: ') + '\n')
		outfile.write('Iris b: ' + b_dim + '\n')
	elif iris_type == 'c':
		outfile.write('Iris l: ' + raw_input('Iris l dimension: ') + '\n')
		outfile.write('Iris a: ' + a_dim + '\n')
		outfile.write('Iris b: ' + raw_input('Iris b dimension: ') + '\n')
	elif iris_type == 'a':
		outfile.write('Iris l: ' + raw_input('Iris l dimension: ') + '\n')
		outfile.write('Iris a: ' + raw_input('Iris a dimension: ') + '\n')
		outfile.write('Iris b: ' + raw_input('Iris b dimension: ') + '\n')
	if ports == 'y':
		outfile.write('Port 1 penetration: ' + raw_input('Port 1 vertical penetration distance: ') + '\n')
		outfile.write('Port 2 penetration: ' + raw_input('Port 2 vertical penetration distance: ') + '\n')
		outfile.write('Port 1 x center: ' + raw_input('Port 1 x center: ') + '\n')
		outfile.write('Port 1 z center: ' + raw_input('Port 1 z center: ') + '\n')
		outfile.write('Port 2 x center: ' + raw_input('Port 2 x center: ') + '\n')
		outfile.write('Port 2 z center: ' + raw_input('Port 2 z center: ') + '\n')
	else:
		pass

