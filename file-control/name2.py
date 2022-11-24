import os
files_path = "./part2/"
files = os.listdir(files_path)

for file in files:
    # print(file)
    # print(len(file))
    '''
    if len(file) == 45:
        old_name = files_path + file
        new_name = files_path + file[:6] + '_타블로와_꿈꾸는_라디오_' + file[33] + '-' + file[36] + '부_' + file[40] + '.mp3'
        os.rename(old_name, new_name)
        # print(old_name, new_name)
    '''
    if len(file) == 43:
        old_name = files_path + file
        new_name = files_path + file[:6] + '_타블로와_꿈꾸는_라디오_' + file[33] + '-' + file[36] + '부' + '.mp3'
        # print(old_name, new_name)
        os.rename(old_name, new_name)