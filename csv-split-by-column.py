import csv
import os

input_filename = 'samples/input.csv'
output_filename_template = ''
split_on_column = 'county'

run_directory = os.path.dirname(os.path.abspath(__file__))
output_directory = run_directory

# open input csv
with open(input_filename, 'rU') as input_file:

	reader = csv.DictReader(input_file)

	for input_row in reader:
		output_filename = os.path.join(
			output_directory,
			input_row[split_on_column] + '.csv'
		)

		if os.path.exists(output_filename) is False:
			output_file = open(output_filename, 'w')
			writer = csv.DictWriter(
				output_file,
				delimiter=',',
				fieldnames=reader.fieldnames
			)
			writer.writeheader()
		else:
			output_file = open(output_filename, 'a')
			writer = csv.DictWriter(
				output_file,
				delimiter=',',
				fieldnames=reader.fieldnames
			)

		writer.writerow(input_row)
