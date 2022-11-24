import os
files_path = "./new/"
files = os.listdir(files_path)

for file in files:
    # if len(file) == 25:
    #     old_name = files_path + file
    #     new_name = files_path + file[6:12] + '_타블로와_꿈꾸는_라디오_' + file[13] + '-' + file[14] + '부_' + file[20]
    #     os.rename(old_name, new_name)
    if len(file) == 26:
        name = files_path + file
        new_name = name + '.mp3'
        os.rename(name, new_name)