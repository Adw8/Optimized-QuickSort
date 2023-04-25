import csv

# Open the CSV file and create a reader object
def getArray(filename, col):
    with open(filename, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)

        # Initialize an empty array to store the values from the column
        column_values = []
        next(csv_reader)

        # Loop through each row in the CSV file
        for row in csv_reader:

            # Append the value in the first column to the column_values array
            column_values.append(float(row[col]))
        column_values.pop(0)
    # Print the column_values array
    return column_values
