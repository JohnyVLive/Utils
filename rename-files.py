""" This script finds number in the middle of file name which starts with # symbol
and adds this number to the beginning of file name.

Instruction:
1. Copy file rename-files.py to target folder
2. Run in shell with command: python3 rename-files.py

Script will find all files in directory and rename them.
"""

import os
import re

current_dir = os.getcwd() + '/'
files_list = os.listdir(current_dir)

for file in files_list:
    number_with_hash = re.findall('#[0-9]+', file)
    if number_with_hash:
        number = re.findall('[0-9]+', number_with_hash[0])
        file_new = number[0] + ' ' + file
        os.rename(current_dir + file, current_dir + file_new)
