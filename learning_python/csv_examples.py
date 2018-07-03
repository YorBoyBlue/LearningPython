import csv

# Approach with regular reader/writer
# with open('../resources/test2.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#
#     with open('../resources/new_test.csv', 'w') as new_file:
#         # Create new file with a different delimiter separator
#         csv_writer = csv.writer(new_file, delimiter='\t')
#
#         # Forces the iterator to go to the next index so that when we loop we
#         # skip the first line in the csv file (headers)
#         # next(csv_reader)
#
#         for line in csv_reader:
#             # You can pass in an index to access a specific column from
#             # each line
#             # print(line[1])
#             # print(line)
#             csv_writer.writerow(line)


# Approach with Dictionary reader/writer
with open('../resources/test2.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('../resources/new_test.csv', 'w') as new_file:
        # Create fieldnames for the Dictionary Writer
        fieldnames = ['first_name', 'last_name']
        # Create new file
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)

        # Force the DictWriter to write the headers first
        csv_writer.writeheader()

        for line in csv_reader:
            # You can choose to delete a column value before writing it if you
            # need to. You should delete it from the fieldnames array if you
            # want the header to not show up as well
            # del line['last_name']
            csv_writer.writerow(line)
