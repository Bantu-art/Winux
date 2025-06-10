import os

class PWD:
    def execute(self, args=None):
        """Print working directory"""
        return os.getcwd()