class SquareAndCube:
    def __init__(self, file_name):
        self.file_name = file_name

    def transform(self):
        with open(self.file_name, 'r') as input_file:
            number_list = list(map(int, input_file.read().split()))