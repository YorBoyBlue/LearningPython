import csv

# Second arg is for what we want to be able to do with the file when we open it
# 'r'   - Read
# 'w'   - Write
# 'r+'  - Read and Write
# 'a'   - Append
# When opening a file in the way we did above we must explicitly close a file
# when you are done with it. Instead, we can use a context manager.
# Example below...
# f = open('../resources/test.txt', 'r')

# print('This file is named: ', f.name)
# print('This files mode is: ', f.mode)

# Close the file. Not needed with the example below
# f.close()

# READING FILES ---------------------------------------------------------------

# Using context manager
with open('../resources/test.txt', 'rb') as f:
    print('This file is named: ', f.name)
    print('This files mode is: ', f.mode)

    # Reads entire file contents - SLOW
    # This can be slow because all of the contents of the file must be read
    # before it returns a result
    contents = f.read()
    print()
    print('What are the contents of this file? (SLOW): ->')
    print(contents.decode("utf-8"))

    # Set the cursor to the beginning of the file
    print()
    print('Your cursor is currently on character: ', f.tell(),
          '(End of the file) or (EOF)')
    print('You have seeked to character: ', f.seek(0, 0))

    # Reads entire file contents - FASTER
    # This is faster because it will read one line at a time and return the
    # result
    print()
    print('What are the contents of this file? (FASTER): ->')
    for line in f:
        print(line.decode("utf-8"), end='')

    # Reads entire file contents - FASTER and more CONTROL
    # This faster and we have more control over how fast we need it to be
    # because we can specify how much of the file to read at a time in
    # byte chucks(characters)
    # When the file object reads past the end of the file it will return an
    # empty string
    print('\n')
    print('What are the contents of this file? (FASTER + CONTROL): ->')
    # Set the cursor to the beginning of the file
    f.seek(0, 0)
    chunk_size = 100
    contents = f.read(chunk_size)
    while len(contents) > 0:
        print(contents.decode("utf-8"), end='')
        contents = f.read(chunk_size)

    # Set the cursor to the beginning of the file
    f.seek(0, 0)

    # returns a list of each line in the file from where the cursor is to the
    # end of the file
    all_lines = f.readlines()
    print('\n')
    print('What are the byte list elements for the lines in this file?: ->')
    print(all_lines)
    print()
    print('What are the string list elements for the lines in this file?: ->')
    for line in all_lines:
        # rstrip() will strip the character passed in from the string if it is
        # on the end of the string. Can used to strip escape chars when
        # they're not wanted. If nothing is passed in it will strip the
        # whitespace by default.
        # print(line.decode("utf-8").rstrip('\n'))
        # You can also pass a kwarg to the print() to accomplish the above
        print(line.decode("utf-8"), end='')
    print('\n\nHow many lines are in the file?: ', len(all_lines), '\n')

    # Reset the cursor to a specific location in the file
    # In this case it is the first character of the first line (negative value
    # in the first arg in end of file. NOTE: This can only be used when opening
    # a file in byte mode)
    f.seek(-3, 2)

    # returns a list of each line in the file from where the cursor is to the
    # end, or a specified amount passed in
    lines = f.readlines()
    print('What are the last 3 chars of this file?: ->')
    for line in lines:
        print(line.decode("utf-8"))

# With the above example using the context manager, we don't need to explicitly
# close the file when done. It is handled for us.
print('\nIs the file closed?: ', f.closed)
print('\n')

# WRITING FILES ---------------------------------------------------------------

# csv ============================

with open('../resources/test2.csv', 'r+', newline='', encoding='utf-8') as f:
    my_contents = [['Learn Python', 'Training', '-More file objects'],
                   ['TSA-169: Fix perms for account swwitching from broker to '
                    'agent', 'killed that task'],
                   ['test', 'testing']]
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(f, fieldnames)
    reader = csv.reader(f)
    # for row in reader:
    #     for column in reader:
    #         for content in my_contents:
    #             for element in content:
    #                 writer.writerow([content])
    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

# txt ============================

# This will copy a files contents to another
with open('../resources/test2.txt', 'w', newline='', encoding='utf-8') as wf:
    with open('../resources/test.txt', 'r', encoding='utf-8') as rf:
        for line in rf:
            wf.write(line)

# images =========================

# This will copy an images content as bytes to another file (must work in bytes
# to use this with images)
with open('../resources/test_copy.jpeg', 'wb') as wf:
    with open('../resources/test.jpeg', 'rb') as rf:
        for line in rf:
            # Slower because whole image has to be read and written before it
            # returns the result
            # wf.write(line)

            # Faster because we are working in chunks
            chunk_size = 4096
            rf_chunk = rf.read(chunk_size)
            while len(rf_chunk) > 0:
                wf.write(rf_chunk)
                rf_chunk = rf.read(chunk_size)
