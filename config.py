"""
Author: Fatih Baday
Email: fatih.baday@outlook.com
Purpose: Get constant variable from 'config.yml' file.
"""

# Loading libraries.
import os
import yaml

# Define constant variables.
CONFIG_FILE_NAME = 'config.yml'


class constant:
    def __init__(self):
        # Get variable from file.
        self.variables = None
        with open(os.path.join(os.getcwd(), CONFIG_FILE_NAME), 'r') as file:
            self.variables = yaml.safe_load(file)
