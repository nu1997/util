import os

dir = os.getcwd()

for file in os.listdir(dir):
    if file[-3:] == 'png':
        old_name = dir + '/' + file
        new_name = dir + '/' + file[-12:]
        os.rename(old_name, new_name)
    # print(new_name)