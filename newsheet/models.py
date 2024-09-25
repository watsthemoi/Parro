

class Model:
    def __init__(self):
        super().__init__()

    def load_file_data(self, path):
        with open(path, 'r') as file:
            self.data = file.read()    