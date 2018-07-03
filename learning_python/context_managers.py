from contextlib import contextmanager


class OpenFile:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with OpenFile('../resources/test.txt', 'w') as f:
    f.write('TESTING!!')

print(f.closed)


@contextmanager
def open_file(file, mode):
    # try and finally insures that if we runt into any errors in the file setup
    # or working with it that we still close the file properly
    try:
        file = open(file, mode)
        yield file
    finally:
        f.close()


with open_file('../resources/test.txt', 'w') as f:
    f.write('OTHER TESTING!!')

print(f.closed)


