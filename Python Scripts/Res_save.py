################################################################### 
# Script for recording results of simulations of RADES structures #
# Author: Cristian Cogollos                                       #
# Last Edition: 23-04-2018                                        #
###################################################################

output_file = raw_input('Introduce the output file name (with its extension): ')
modes = int(raw_input('Number of modes to record: '))

#Recording the results into the output file
with open(output_file,"w") as outfile:

	for i in range(43):
		outfile.write('#')
	outfile.write('\n')
	outfile.write('# Results file for a given RADES geometry #\n')
	for i in range(43):
		outfile.write('#')
	outfile.write('\n\n')

	for i in range(19):
		outfile.write('#')
	outfile.write('\n')
	outfile.write('# Physics Results #\n')
	for i in range(19):
		outfile.write('#')
	outfile.write('\n')
	outfile.write('Number of modes: ' + str(modes) + '\n\n')
	for i in range(modes):
		outfile.write('*Mode ' + str(i+1) + '*\n')
		print('\n*Mode ' + str(i+1) + '*')
		outfile.write('Frequency: ' + raw_input('Frequency: ')+ '\n')
		option = raw_input('Do you want to record the rest of resutls for this mode?(y/n) ')
		if option == 'y' or option == 'Y':
			outfile.write('C^2: ' + raw_input('C^2: ') + '\n')
			outfile.write('Q: ' + raw_input('Q: ') + '\n')
			outfile.write('F.O.M.: ' + raw_input('F.O.M.: ') + '\n')
		else:
			pass
		outfile.write('\n')
	option = raw_input('Do you want to introduce the simulation parameters?(y/n) ')
	if option == 'y' or option == 'Y':
		for i in range(22):
			outfile.write('#')
		outfile.write('\n')
		outfile.write('# Simulation Details #\n')
		for i in range(22):
			outfile.write('#')
		outfile.write('\n')
		outfile.write('**Mesh Adaptation Properties**\n')
		print('\n**Mesh Adaptation Properties**')
		outfile.write('Max. freq. variation: ' + raw_input('Max. freq. variation: ') + '\n')
		outfile.write('Min. number of passes: ' + raw_input('Min. number of passes: ') + '\n')
		outfile.write('Max. number of passes: ' + raw_input('Max. number of passes: ') + '\n')
		outfile.write('Number of modes to check: ' + raw_input('Number of modes to check: ') + '\n\n')
		outfile.write('**Eigenmode solver specials**\n')
		print('\n**Eigenmode solver specials**')
		outfile.write('Accuracy: ' + raw_input('Accuracy: ') + '\n')
		outfile.write('Solver order: ' + raw_input('Solver order: ') + '\n\n')
		outfile.write('**Mesh Properties**\n')
		outfile.write('*Cells per wavelength*\n')
		print('\n**Mesh Properties**')
		print('*Cells per wavelength*')
		outfile.write('Model: ' + raw_input('Model: ') + '\n')
		outfile.write('Background: ' + raw_input('Background: ') + '\n\n')
		outfile.write('*Cells per max model box edge*\n')
		print('\n*Cells per max model box edge*')
		outfile.write('Model: ' + raw_input('Model: ') + '\n')
		outfile.write('Background: ' + raw_input('Background: ') + '\n\n')
		print('\n')
		outfile.write('Minimum cell: ' + raw_input('Minimum cell: ') + '\n')
		outfile.write('Meshing method: ' + raw_input('Meshing method: '))

	else:
		pass
outfile.close()
