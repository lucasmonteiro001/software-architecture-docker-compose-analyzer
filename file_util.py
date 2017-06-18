import os


class FileUtil(object):
    @staticmethod
    def get_files_from_directory(directory):
        return map(lambda f: directory + "/" + f, os.listdir(directory))
