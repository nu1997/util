# import xml.etree.ElementTree as ET
from lxml import etree
import os
import wget

file_names = os.listdir('./xml')
# print(file_names)


for file_name in file_names:
    # tree = ET.parse(f'./xmls/{file_name}')
    # root = tree.getroot()
    tree = etree.parse(f'./xml/{file_name}')
    root = tree.getroot()

    for i in range(10):
        try:
            url = root[0][i][2].text
            original = root[0][i][1].text
            title = original[:-10].strip()
            date = original[-8:].strip()
            year = date[:2]
            month = date[3:5]
            day = date[6:8]
            fixed_date = year + '-' + month + '-' + day
            name = fixed_date + ' ' + title
            # wget.download(url, f'./{date}_{title}_{i+1}.mp3')
            wget.download(url, f'./mp3/{name}_{i+1}.mp3')
        except Exception as e:
            print(e)
            continue