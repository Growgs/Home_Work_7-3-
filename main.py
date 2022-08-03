import os
import glob

DIR_NAME = os.getcwd()
pattern = '*.txt'
new_file = 'new_file.txt'
path = os.path.join(DIR_NAME, pattern)
file_list = glob.glob(path)
file_list = sorted(file_list, key=lambda x: os.stat(os.path.join(DIR_NAME, x)).st_size)
for file_name in file_list:
    with open(file_name) as file_read, open(new_file, 'a') as file_write:
        text = file_read.read()
        count_lines = text.count('\n') + 1
        file_write.write(f'\n{os.path.basename(file_name)}\n{count_lines}\n')
        for line in text:
            file_write.write(line)