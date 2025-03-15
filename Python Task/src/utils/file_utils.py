import os

class FileUtils:
    @staticmethod
    def get_file_path(filename):
        return os.path.join(os.getcwd(), "data", filename)
